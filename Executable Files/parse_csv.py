import csv
import shutil
from dotenv import load_dotenv
import os

# Creates output CSV, which will be altered using a writer object
def create_output_csv(csv_src_path, csv_dst_path):
    shutil.copyfile(csv_src_path, csv_dst_path)
    
# Utility function for debugging
def print_headers(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print('\n'.join(row))

def main():
    load_dotenv()
    csv_src_path = os.environ.get('CSV_SRC_PATH')
    csv_dst_path = os.environ.get('CSV_DST_PATH')
    create_output_csv(csv_src_path, csv_dst_path)
    print_headers(csv_src_path)

main()