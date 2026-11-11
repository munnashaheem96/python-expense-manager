
import csv


def write_to_file(data):

    with open(
        "expenses.txt",
        "w",
        newline="",
        encoding="utf-8"
    ) as fp:

        writer = csv.writer(fp)
        writer.writerows(data)


def read_data_from_file():

    data = []

    try:
        with open(
            "expenses.txt",
            "r",
            newline="",
            encoding="utf-8"
        ) as fp:

            reader = csv.reader(fp)

            for row in reader:

                if len(row) == 4:

                    try:
                        data.append((
                            row[0],
                            row[1],
                            int(row[2]),
                            row[3]
                        ))

                    except ValueError:
                        continue

    except FileNotFoundError:
        print("No previous data found.")

    return data
