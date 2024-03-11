import csv
import shutil
from dotenv import load_dotenv
import os

# Utility function for debugging
def print_headers(csv_path):
    with open(csv_path, newline='') as csvfile:
        headers = csv.reader(csvfile, delimiter=',', quotechar='|')
        for column in headers:
            print('\n'.join(column))

# Creates output CSV, which will be altered using a writer object
def create_output_csv(csv_path):
    shutil.copyfile(csv_path, 'Donor_Information_Executable/Output CSVs/Donor Information.csv')

def main():
    load_dotenv()
    csv_path = os.environ.get('CSV_PATH')
    print_headers(csv_path)
    #create_output_csv(csv_path)

main()