import csv

with open("names.csv", "r") as csv_file:

    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)

    with open("new_dict_writer.csv", "w") as new_file:
        fieldnames = ["first_name", "last_name"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line1 in csv_reader:
            del line1["email"]
            csv_writer.writerow(line1)


