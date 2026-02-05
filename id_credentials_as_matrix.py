import csv

def print_csv_as_matrix(csv_file):
    matrix = []
    with open(csv_file,"r") as f:
        csv_obj = csv.reader(f)
        matrix.append(next(csv_obj))
        for row in csv_obj:
            matrix.append(row)
        print(matrix)
print_csv_as_matrix("credentials.csv")