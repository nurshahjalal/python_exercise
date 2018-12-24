import csv

with open("names.csv", "r") as csv_file:

    csv_reader = csv.reader(csv_file)

    print(csv_reader)

    with open("new_names.csv", "w") as new_csv:
        csv_writer = csv.writer(new_csv, delimiter="\t")
        for line in csv_reader:
            csv_writer.writerow(line)

with open('new_names.csv', "r") as new_csv_read:
    new_csv_reader = csv.reader(new_csv_read, delimiter='\t')

    for line in new_csv_reader:
        print(line)


