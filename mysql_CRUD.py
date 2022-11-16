# CRUD OPERATION IN MYSQL USING PYTHON
from prettytable import PrettyTable
from mysql_transactions import get_user_data, add_new_user_data, update_user_data, delete_user_data


def get_user_inputs(action=None):
    try:
        if action != "delete":
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            city = input("Enter CITY : ")
            res = (name, age, city)
            if action:
                id = int(input("Enter ID : "))
                res = (name, age, city, id)
        else:
            res = int(input("Enter ID : "))
    except Exception as e:
        print("Please give correct values")
        print(f"ERROR : {e}")

    return res


def get_user_details():
    users_data = get_user_data()
    if users_data:
        table = PrettyTable(["ID", "NAME", "AGE", "CITY"])
        table.add_rows([i for i in users_data])
        print(table)


def add_new_user():
    name, age, city = get_user_inputs()
    print(add_new_user_data(name, age, city))
    get_user_details()

def update_user_details():
    name, age, city, id = get_user_inputs("update")
    update_user_data(name, age, city, id)
    get_user_details()


def remove_user_details():
    id = get_user_inputs("delete")
    delete_user_data(id)
    get_user_details()

# USER INTERFACE
def display_fun_info():
    table = PrettyTable(["Create", "Update", "Delete", "Select"])
    table.add_row(("1 . Create User (1)",
                   "2 . Update User (2)",
                   "3 . Delete User (3)",
                   "4 . Select User Table (4)"))
    print(table)
def display_greetings():
    print("""
                    *************************************************
                            Thank you for using our services.
                        Be in touch..!              Be happy..!
                    *************************************************
    """)


# MAIN LOOP
while True:
    display_fun_info()
    try:
        ch = int(input("Enter your choice : "))
    except:
        print("You have entered INVALID VALUE")
        continue
    if ch==1:
        add_new_user()
    elif ch == 2:
        update_user_details()
    elif ch == 3:
        remove_user_details()
    elif ch == 4:
        get_user_details()
    else:
        print("You have entered INVALID KEY VALUE")
        continue
    ex = input("Do you want to continue this process press (y/Y) : ")
    if ex.upper() != "Y":
        break

display_greetings()
