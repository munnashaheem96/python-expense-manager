
def write_to_file(c):
    with open("expenses.txt", "w") as fp:
        for item in c:
            data = f"{item[0]} {item[1]} {item[2]} {item[3]}\n"
            fp.write(data)


def read_data_from_file():
    ct = []

    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                s = line.split()

                if len(s) == 4:
                    ct.append((s[0], s[1], int(s[2]), s[3]))

    except FileNotFoundError:
        print("No previous expense file found. Starting fresh.")

    return ct
