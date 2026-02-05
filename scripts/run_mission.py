#!/usr/bin/env python3
"""
AFSIM Mission Executor
Wrapper script to execute AFSIM mission.exe with proper error handling and output capture.
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path

# AFSIM installation directory
AFSIM_DIR = r"D:\Program Files\afsim2.9.0"
MISSION_EXE = os.path.join(AFSIM_DIR, "bin", "mission.exe")

def run_mission(script_file, options=None):
    """
    Execute AFSIM mission.exe with the given script file.

    Args:
        script_file: Path to the .wsf script file
        options: List of command-line options (e.g., ['-es', '-fio'])

    Returns:
        tuple: (return_code, stdout, stderr)
    """
    if not os.path.exists(MISSION_EXE):
        print(f"ERROR: mission.exe not found at {MISSION_EXE}", file=sys.stderr)
        print(f"Please verify AFSIM installation directory", file=sys.stderr)
        return 1, "", f"mission.exe not found at {MISSION_EXE}"

    if not os.path.exists(script_file):
        print(f"ERROR: Script file not found: {script_file}", file=sys.stderr)
        return 1, "", f"Script file not found: {script_file}"

    # Build command
    cmd = [MISSION_EXE]
    if options:
        cmd.extend(options)
    cmd.append(script_file)

    print(f"Executing: {' '.join(cmd)}")
    print("-" * 80)

    try:
        # Run mission.exe
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(script_file)) or "."
        )

        # Print output
        if result.stdout:
            print(result.stdout)

        if result.stderr:
            print("STDERR:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)

        print("-" * 80)
        print(f"Exit code: {result.returncode}")

        return result.returncode, result.stdout, result.stderr

    except Exception as e:
        error_msg = f"Failed to execute mission.exe: {str(e)}"
        print(f"ERROR: {error_msg}", file=sys.stderr)
        return 1, "", error_msg

def main():
    parser = argparse.ArgumentParser(
        description="Execute AFSIM mission.exe with a script file"
    )
    parser.add_argument(
        "script_file",
        help="Path to the .wsf script file"
    )
    parser.add_argument(
        "-es",
        action="store_true",
        help="Event-stepped mode (default)"
    )
    parser.add_argument(
        "-rt",
        action="store_true",
        help="Real-time frame-stepped mode"
    )
    parser.add_argument(
        "-fs",
        action="store_true",
        help="Non-realtime frame-stepped mode"
    )
    parser.add_argument(
        "-fio",
        action="store_true",
        help="Flush output"
    )
    parser.add_argument(
        "-sm",
        action="store_true",
        help="Suppress messages"
    )
    parser.add_argument(
        "-mi",
        type=int,
        metavar="INTERVAL",
        help="Message interval"
    )

    args = parser.parse_args()

    # Build options list
    options = []
    if args.es:
        options.append("-es")
    if args.rt:
        options.append("-rt")
    if args.fs:
        options.append("-fs")
    if args.fio:
        options.append("-fio")
    if args.sm:
        options.append("-sm")
    if args.mi:
        options.extend(["-mi", str(args.mi)])

    # Run mission
    return_code, stdout, stderr = run_mission(args.script_file, options)

    sys.exit(return_code)

if __name__ == "__main__":
    main()
