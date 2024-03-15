import csv
# Used for outputting a copy of the template CSV
from shutil import copyfile
# If unable to pip install this python module, look into brew install
# Used for protecting paths from public environments
from dotenv import load_dotenv
from os import environ

# Creates output CSV, which will be altered using a writer object
def create_output_csv(csv_src_path, csv_dst_path):
    copyfile(csv_src_path, csv_dst_path)
    
# Returns field names for mapping inputs from the GUI
def create_keys(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        keys = list()
        # Important to use extend rather than append in this instance
        for column in reader:
            keys.extend(column)
        return keys

def main():
    load_dotenv()
    csv_src_path = environ.get('CSV_SRC_PATH')
    csv_dst_path = environ.get('CSV_DST_PATH')
    create_output_csv(csv_src_path, csv_dst_path)
    global keys
    keys = create_keys(csv_src_path)

main()