import os

class Colors:
    """
    Provides ANSI escape codes for colored output.

    Attributes:
        CYAN (str): ANSI escape code for cyan color.
        RED (str): ANSI escape code for red color.
        GREEN (str): ANSI escape code for green color.
        ORANGE (str): ANSI escape code for orange color.
        BLUE (str): ANSI escape code for blue color.
        YELLOW (str): ANSI escape code for yellow color.
        PURPLE (str): ANSI escape code for purple color.
        NORMAL (str): ANSI escape code to reset color to default.
    """
    CYAN = '\033[96m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    ORANGE = '\033[1;33m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    NORMAL = '\033[0m'

    @staticmethod
    def supports_ansi():
        """Check if the terminal supports ANSI escape codes."""
        return os.getenv('ANSICON') is not None or os.getenv('TERM') == 'xterm' or 'COLORTERM' in os.environ


HANGMAN_STAGES = [
    f"""{Colors.CYAN}
  +---+
  |   |
      |
      |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.CYAN}
  +---+
  |   |
  O   |
      |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.CYAN}
  +---+
  |   |
  O   |
  |   |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.CYAN}
  +---+
  |   |
  O   |
 /|   |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.CYAN}
  +---+
  |   |
  O   |
 /|\  |
      |
      |
{Colors.NORMAL}
""",
    f"""{Colors.ORANGE}
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
{Colors.NORMAL}
""",
    f"""{Colors.RED}
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
{Colors.NORMAL}
"""
]

def render_hangman_graphic(attempts, level):
    """
    Renders the hangman graphic based on the current difficulty level.
    """
    valid_levels = ['easy', 'medium', 'hard']
    if not isinstance(level, str) or level not in valid_levels:
     raise ValueError(f"Invalid level: {level}. Must be one of {valid_levels}.")
 
    max_attempts = len(HANGMAN_STAGES) - 1
    
    if not (0 <= attempts <= max_attempts):
        raise ValueError(f"Invalid number of attempts: {attempts}. Must be between 0 and {max_attempts}.")
