
from helper import *
from fileop import *

y = 0

kdata = read_data_from_file()
set_expense(kdata)

while y == 0:
    opt = menu()

    if opt == 1:
        add_expense()

    elif opt == 2:
        display_expense()

    elif opt == 3:
        delete_expense()

    elif opt == 4:
        update_expense()

    elif opt == 5:
        add_income()

    elif opt == 6:
        view_balance()

    else:
        print("Invalid Option")

    # Save data after every operation
    data1 = get_expense()
    write_to_file(data1)

    try:
        y = int(input("Do you want to continue? (Press 0 for yes): "))
    except ValueError:
        y = 1

print("Program Closed!")
