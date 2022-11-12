# CRUD OPERATION IN SQL USING PYTHON
from prettytable import PrettyTable
from crud_transactins import CrudDataBase

db_obj = CrudDataBase()

funNames = "insert,update,delete,select".split(',')

# PYTHON FUNCTIONS

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


def insert_record():
    name, age, city = get_user_inputs()
    db_obj.insertQRY(name,age,city)
    print("User record inserted successfully.")
    db_obj.close_db_connection()


def update_record():
    name, age, city, id = get_user_inputs("update")
    db_obj.updateQRY(name, age, city, id)
    print("User record updated successfully.")
    select_record()


def delete_record():
    db_obj.deleteQRY(get_user_inputs("delete"))
    print("User record deleted successfully.")
    db_obj.close_db_connection()


def select_record():
    usersData = db_obj.selectQRY()
    table = PrettyTable(["ID","NAME","AGE","CITY"])
    table.add_rows([data for data in usersData])
    print(table)
    db_obj.close_db_connection()


# USER INTERFACE
def display_fun_info():
    table = PrettyTable(["Create", "Update", "Delete", "Select"])
    table.add_row(("1 . Create a new record press (1)",
                   "2 . Update the existing data press (2)",
                   "3 . Delete the record press (3)",
                   "4 .See the table press (4)"))
    print(table)
def display_greetings():
    print("""
                    *************************************************
                            Thank you for using our servies.
                        Be in touch..!              Be happy..!
                    *************************************************
    """)


# MAIN LOOP
while True:
    display_fun_info()
    try:
        key = int(input("Enter the Value : "))
        key = "" if key<=0 else key
        # CALLING FUNCTION
        eval(f"{funNames[key-1]}_record")()
    except:
        print("You have entered INVALID VALUE")
    finally:
        exit = input("Do you want to exit press (Y/y) : ")
        if exit.upper() == "Y":
            break

display_greetings()