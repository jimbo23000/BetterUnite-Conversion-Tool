from dotenv import load_dotenv
from os import environ
from gui import *

# Executes the application
def main():
    load_dotenv()
    GUI(environ.get('CSV_SRC_PATH'), environ.get('CSV_DST_PATH'))

main()