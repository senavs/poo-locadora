import os


def clear_shell():
    """Clear shell terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
