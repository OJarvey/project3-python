import random
import gspread
from google.oauth2.service_account import Credentials
from visuals import (
        display_title, 
        display_victory, 
        display_defeat, 
        render_hangman_graphic, 
        Colors
)

# Constants
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Google Sheets API Setup
CREDENTIALS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDENTIALS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('guess-or-hang')

# Utility Functions
def fetch_word() -> str:
    """Fetches a random word from Google Sheets."""
    try:
        sheet = GSPREAD_CLIENT.open('guess-or-hang').sheet1
        word_list = sheet.col_values(1)
        if not word_list:
            raise ValueError("Word list is empty. Please add words to the spreadsheet.")
        return random.choice(word_list).lower()
    except gspread.exceptions.APIError as e:
        raise ValueError(f"Error accessing Google Sheets: {e}")
    except gspread.exceptions.SpreadsheetNotFound as e:
        raise ValueError(f"Spreadsheet 'guess-or-hang' not found: {e}")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")