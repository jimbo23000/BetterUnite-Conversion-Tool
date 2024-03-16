import csv

# Returns the field names used for creating dictionary entries
def create_keys(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        keys = list()
        # Important to use extend rather than append in this instance
        for column in reader:
            keys.extend(column)
        return keys
    
# Will create the output CSV based on the template CSV's keys and user inputted values
def create_output_csv(csv_path, keys, csv_row_entries):
    with open(csv_path, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for csv_row_entry in csv_row_entries:
            writer.writerow(csv_row_entry)