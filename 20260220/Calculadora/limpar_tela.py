import os

def clear_terminal():
    """Clears the terminal screen for Windows, Linux, and macOS."""
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux and macOS (posix)
        _ = os.system('clear')