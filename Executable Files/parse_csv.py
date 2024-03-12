import os
import csv
import shutil

from dotenv import load_dotenv

# Creates output CSV, which will be altered using a writer object
def create_output_csv(csv_src_path, csv_dst_path):
    shutil.copyfile(csv_src_path, csv_dst_path)
    
# Returns field names for mapping inputs from the GUI
def create_dict(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        field_names = list()
        for column in reader:
            field_names.append(column)
        #for element in dict:
        #   print(', '.join(element))
        return field_names

def main():
    load_dotenv()
    csv_src_path = os.environ.get('CSV_SRC_PATH')
    csv_dst_path = os.environ.get('CSV_DST_PATH')
    create_output_csv(csv_src_path, csv_dst_path)
    global field_names
    field_names = create_dict(csv_src_path)

main()