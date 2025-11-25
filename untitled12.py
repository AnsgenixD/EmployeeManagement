import pandas as pd
import random
import os

#password is admin and the filename should ideally be employees.csv
password = "admin"
current_folder = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_folder, "employees.csv")



def MakeRandomID(df):
    #making a random employee id
    rid = random.randint(1000, 9999)

    if len(df) > 0:
        while rid in df['EmployeeID'].values:
            rid = random.randint(1000, 9999)

    return rid

def add_user():
    n = input("Enter Employee Name: ")

    #open file to read if duplicates exist
    if os.path.exists(filename):
        df = pd.read_csv(filename)
    else:
        df = pd.DataFrame(columns=['Name', 'EmployeeID'])
    #after opening the file, make a unique id for it.


    
    employeeid = MakeRandomID(df)

    #making a new row under the existing columns: Name, and EmployeeID
    new_row = {'Name': n, 'EmployeeID': employeeid}

    # Add it to the table
    df.loc[len(df)] = new_row

    # Save
    df.to_csv(filename, index=False)
    print("Success! Saved " + n + " with Random ID: " + str(employeeid))

def show_list():
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        print("----------------")
        print(df)
        print("----------------")
    else:
        print("File not found.")

def update_user():
    p = str(input("Enter Password: "))

    if p == password:
        show_list()

        pid = int(input("Enter the ID Number you want to fix: "))

        df = pd.read_csv(filename)

        # Check if that random ID exists
        if pid in df['EmployeeID'].values:
            new_name = input("Enter the correct name: ")
            df.loc[df['EmployeeID'] == pid, 'Name'] = new_name
            df.to_csv(filename, index=False)
            print("Updated successfully.")
        else:
            print("ID not found.")
    else:
        print("Wrong password.")


while True:
    os.system('cls' if os.name == 'nt' else 'clear') #Pulling up this menu will clear screen to make it look clean.
    print("\n--- Manager Window ---")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. View All")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_user()
        input("Press Enter to continue...")
    elif choice == "2":
        update_user()
        input("Press Enter to continue...") 
    elif choice == "3":
        show_list()
        input("Press Enter to continue...") 
    elif choice == "4":
        break
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to continue...")
