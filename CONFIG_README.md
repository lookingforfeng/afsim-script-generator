# Configuration Guide

## config.txt - AFSIM Installation Configuration

This file tells the skill where your AFSIM installation is located.

### Configuration Format

```
# AFSIM Installation Directory
# This is the root directory where AFSIM is installed
# All other paths are derived from this base directory
AFSIM_INSTALL_DIR=D:\Program Files\afsim2.9.0
```

### What Gets Configured

When you set `AFSIM_INSTALL_DIR`, the following paths are automatically derived:

1. **mission.exe**: `{AFSIM_INSTALL_DIR}/bin/mission.exe`
   - Used to execute AFSIM scripts
   - Called by `scripts/run_mission.py`

2. **Documentation**: `{AFSIM_INSTALL_DIR}/documentation/html/docs`
   - Contains 1602 official AFSIM HTML documentation files
   - Ultimate reference for detailed information
   - Used when skill documentation doesn't cover specific details

### How to Configure

#### On Windows
```
AFSIM_INSTALL_DIR=D:\Program Files\afsim2.9.0
```

#### On Linux/Mac (if applicable)
```
AFSIM_INSTALL_DIR=/opt/afsim2.9.0
```

### Using on Different Computers

When moving this skill to a different computer:

1. Copy the entire skill directory
2. Open `config.txt`
3. Update `AFSIM_INSTALL_DIR` to match the new computer's AFSIM installation
4. Save the file

That's it! Everything else works automatically.

### Verification

To verify your configuration is correct:

```bash
python scripts/run_mission.py --help
```

This will display:
- Your configured AFSIM installation directory
- The derived mission.exe path
- The derived documentation path

If any path is incorrect, update `AFSIM_INSTALL_DIR` in config.txt.

### Troubleshooting

**Problem**: mission.exe not found

**Solution**:
1. Check that AFSIM is actually installed at the specified path
2. Verify the path in config.txt is correct
3. Make sure `bin/mission.exe` exists under your AFSIM installation

**Problem**: Documentation not found

**Solution**:
1. Check that `documentation/html/docs` exists under your AFSIM installation
2. If documentation is in a different location, you may need to copy it or create a symbolic link

### Default Configuration

If `config.txt` is missing or cannot be read, the skill uses this default:

```
AFSIM_INSTALL_DIR=D:\Program Files\afsim2.9.0
```

### Notes

- Lines starting with `#` are comments and are ignored
- Empty lines are ignored
- Only `AFSIM_INSTALL_DIR` needs to be configured
- All other paths are automatically calculated
- The configuration is read every time you run a script
