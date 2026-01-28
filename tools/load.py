import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

def start_client():

    load_dotenv()
    SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
    SCOPES = ["https://spreadsheets.google.com/feeds", 
          "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive.file", 
          "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)

    return client


class Load:

    def __init__(self, file_name):

        client = start_client()
        self.workbook = client.open(file_name)

    def append_row(self, sheet_name, data):
        """
        Append row to sheet_name
        
        :param sheet_name: Name of work sheet to be modified
        :param data: Data to be appended to work sheet. 
        """
        sheet = self.workbook.worksheet(sheet_name)
        sheet.append_row(data)

if __name__ == "__main__":
    pass