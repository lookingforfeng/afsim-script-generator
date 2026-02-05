#!/usr/bin/env python3
"""
AFSIM Mission Executor
Wrapper script to execute AFSIM mission.exe with proper error handling and output capture.
Reads configuration from config.txt for AFSIM installation directory.
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path

def load_config():
    """
    Load AFSIM configuration from config.txt

    Returns:
        dict: Configuration dictionary with keys:
            - afsim_install_dir: AFSIM installation directory
            - documentation_dir: Documentation directory path
            - mission_exe: mission.exe path
    """
    # Get the skill directory (parent of scripts directory)
    script_dir = Path(__file__).parent
    skill_dir = script_dir.parent
    config_file = skill_dir / "config.txt"

    # Default configuration
    config = {
        "afsim_install_dir": r"D:\Program Files\afsim2.9.0",
        "documentation_dir": None,
        "mission_exe": None
    }

    # Read config file if it exists
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Skip comments and empty lines
                    if not line or line.startswith('#'):
                        continue
                    # Parse key=value
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        if key == "AFSIM_INSTALL_DIR":
                            config["afsim_install_dir"] = value
        except Exception as e:
            print(f"Warning: Failed to read config.txt: {e}", file=sys.stderr)
            print(f"Using default configuration", file=sys.stderr)
    else:
        print(f"Warning: config.txt not found at {config_file}", file=sys.stderr)
        print(f"Using default configuration", file=sys.stderr)

    # Derive other paths from install directory
    install_dir = config["afsim_install_dir"]
    config["documentation_dir"] = os.path.join(install_dir, "documentation", "html", "docs")
    config["mission_exe"] = os.path.join(install_dir, "bin", "mission.exe")

    return config

def run_mission(script_file, options=None, config=None):
    """
    Execute AFSIM mission.exe with the given script file.

    Args:
        script_file: Path to the .txt script file
        options: List of command-line options (e.g., ['-es', '-fio'])
        config: Configuration dictionary (if None, will load from config.txt)

    Returns:
        tuple: (return_code, stdout, stderr)
    """
    if config is None:
        config = load_config()

    mission_exe = config["mission_exe"]

    if not os.path.exists(mission_exe):
        print(f"ERROR: mission.exe not found at {mission_exe}", file=sys.stderr)
        print(f"Please verify AFSIM installation directory in config.txt", file=sys.stderr)
        print(f"Current AFSIM_INSTALL_DIR: {config['afsim_install_dir']}", file=sys.stderr)
        return 1, "", f"mission.exe not found at {mission_exe}"

    if not os.path.exists(script_file):
        print(f"ERROR: Script file not found: {script_file}", file=sys.stderr)
        return 1, "", f"Script file not found: {script_file}"

    # Build command
    cmd = [mission_exe]
    if options:
        cmd.extend(options)
    cmd.append(script_file)

    print(f"AFSIM Configuration:")
    print(f"  Install Dir: {config['afsim_install_dir']}")
    print(f"  Mission.exe: {mission_exe}")
    print(f"  Documentation: {config['documentation_dir']}")
    print()
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
        help="Path to the .txt script file"
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

    # Load configuration
    config = load_config()

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
    return_code, stdout, stderr = run_mission(args.script_file, options, config)

    sys.exit(return_code)

if __name__ == "__main__":
    main()
