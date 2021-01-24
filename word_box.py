import sys, csv
from ascii import print_table
# CSV related methods
def get_num_fields(csvfile):
    """Returns the number of fields in the CSV file. This assumes the number of fields is the same for all records."""
    # Create temp csv reader
    temp_reader = csv.reader(csvfile)
    num_fields = 0 # len(next(temp_reader))
    for line in temp_reader:
        if len(line) > num_fields:
            num_fields = len(line)
    csvfile.seek(0) # Move reader back to start of file, is this needed since I'm using a temp reader?
    return num_fields

# Create outer list to hold list data from reader
csv_data = []
# Get name of file from command line args
try:
    filename = sys.argv[1]
except IndexError as err:
    print('Forgot to provide file name')
    exit()
# Open and parse CSV file into format required for ascii method
with open(filename) as csvfile:
    reader1 = csv.reader(csvfile)
    for line in reader1:
        csv_data.append(line)
print_table(csv_data)
