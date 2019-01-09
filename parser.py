import csv


def read_input(path='dataset_tema3.csv'):
    input_file = open(path, 'r')
    input_csv = csv.reader(input_file)
    header_passed = False
    output = []

    k = 0 # Test purpose only. TODO: Remove

    for line in input_csv:
        if not header_passed:
            header_passed = True
            continue
        output.append(line)

        # Test purpose only. TODO: Remove
        if k < 8:
            print("headline:", line[0], "\ntext:", line[1], "\nctext:", line[2])
            k += 1

    input_file.close()
    return output