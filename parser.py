import csv


def read_input(path='dataset_tema3.csv'):
    input_file = open(path, 'r')
    input_csv = csv.reader(input_file)
    header_passed = False
    output = []

    for line in input_csv:
        if not header_passed:
            header_passed = True
            continue
        output.append(line)

    input_file.close()
    return output
