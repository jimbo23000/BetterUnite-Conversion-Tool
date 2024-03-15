from dotenv import load_dotenv
from os import environ
import parse
from gui import *

# Executes the application
def main():
    load_dotenv()
    csv_src_path = environ.get('CSV_SRC_PATH')
    csv_dst_path = environ.get('CSV_DST_PATH')
    GUI(csv_dst_path, parse.create_keys(csv_src_path))

main()