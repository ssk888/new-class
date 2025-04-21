import sqlite3 
import csv

# CLI => Command Line Interface
# CRUD => Create, Read, Update, Delete
# 80% - 90% CRUD

# go to git bash
# git config --global user.name "Satish Singh Kunwar"
# git config --global user.email "satishsinghkunwar@gmail.com"

# first Time 
#git init => git initialize
#git status => if you want to check what are the status of files
#git diff => if you want to check what are the changes
#git add . => Track all the files
#git commit -m "Your message"
#copy paste git code from github

# 80% - 90% you will do these while working in companies

# 1. change the code
# 2. git add.
# 3. git commit -m "Your Message"
# 4. git push


INPUT_STRING = """
Enter the option:
    1. CREATE TABLE
    2. DUMP users from csv INTO users TABLE
    3. ADD new user INTO users TABLE
    4. QUERY all users from TABLE
    5. QUERY user by id from TABLE
    6. QUERY specified no. of records from TABLE
    7. DELETE all users
    8. DELETE user by id
    9. UPDATE user
    10. Press any key to EXIT
"""

def create_connection():
    try:
        con = sqlite3.connect("users.sqlite3")
    except Exception as e:
        print(e)

    




def create_table(con):
    CREATE_USERS_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             first_name CHAR(255) NOT NULL,
             last_name CHAR(255) NOT NULL,
             company_name CHAR(255) NOT NULL,
             address CHAR(255) NOT NULL,
             city CHAR(255) NOT NULL,
             county CHAR(255) NOT NULL,
             state CHAR(255) NOT NULL,
             zip REAL NOT NULL,
             phone1 CHAR(255) NOT NULL,
             phone2 CHAR(255),
             email CHAR(255) NOT NULL,
             web text 
   );
"""
cur = con.cursor()
cur.execute(CREATE_USERS_TABLE_QUERY)
print("User table was succesfully.")

def read_csv():
    with open("sample.csv", "r") as f:
        data = csv.reader(f)
        for user in data:
            users.append(tuple(user))

    return(user[1:])


def insert_users(con, users):
    user_add_query = """
         INSERT INTO users
         (
            first_name,
            last_name,
            company_name,
            address,
            city,
            county,
            state,
            zip,
            phone1,
            phone2,
            email,
            web
         )
         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
     """
    cur = con.cursor()
    cur.executemany(user_add_query, users)
    con.commit()
    print(f"{len(users)} users were imported successfully.")

def select_all_users(con):

def select_user_by_id(con, user_id):
    cor = con.cursor()
    users = cur.execute("SELECT * FROM users where id = ?;", (user_id))
    for user in users:
        print(user)

def select_specified_no_of_records(con, no_of_records):
    cur = con.cursor()
    users = cur.execute("SELECT * FROM user LIMIT ?;", (no_of_records))
    for user in users:
        print(user)

def select_specified_no_of_records(con, no_of_records):
    cur = con.cursor()
    users = cur.execute("SELECT * FROM users LIMIT ?;", (no_of_records,))
    for user in users:
        print(user)

def delete_users(con):
    cur = con.cursor()
    users = cur.execute("DELETE FROM users;")
    con.commit()
    print("ALL users were deleted successfully")


def delete_user_by_id(con, user_id):
    cur = con.cursor()
    cur.execute("DELETE FROM users where id = ?", (user_id,))
    con.commit()
    print(f"User with id [{user_id}] was successfully deleted.")

COLUMNS = (
            "first_name",
            "last_name",
            "company_name",
            "address",
            "city",
            "county",
            "state",
            "zip",
            "phone1",
            "phone2",
            "email",
            "web",
         )

def update_user_by_id(con, user_id, column_name, column_value):
    cur = con.cursor()
    cur.execute(
        f"UPDATE users set {column_name}=? where id = ?:", (column_value, user_id)
    )
    con.commit()
    print(
        f"[{column_name}] was updated with value [{column_value}] of user with id [{user_id}]"
    )


def main():
    con = create_connection()
    if con is None:
        print("Error! cannot create the database connection.")
        return
    
    user_input = input(INPUT_STRING)
    if user_input == "1":
        create_table(con)
    elif user_input == "2":
       users = read_csv
       insert_users(con, users)
    elif user_input == "3":
        user_data = [] 
        for column in COLUMNS:
            column_value = input(f"Enter the value of (column) :")
            user_data.append(column_value)
        insert_users(con, [tuple(user_data)])    
    elif user_input == "4":
        select_all_users(con)
    elif user_input == "5":
        user_id = input("Enter user id: ")
        if user_id.isnumeric():
            select_user_by_id(con, user_id)
        else:
            print("Invalid user id.")
    elif  user_input == "6":
        no_of_records = input("ENTER no. of records: ")
        if no_of_records.isnumeric():
            select_specified_no_of_records(con, no_of_records)
        else:
            print("Invalid no. of records.") 

    elif user_input == "7":
        confirmation = input("Are you sure you want to delete all users? (y/n): ")
        if confirmation == "y":
            delete_users(con)    
    elif user_input == "8":
        user_id = input("Enter user id: ")
        if user_id.isnumeric():
            delete_user_by_id(con, user_id)
    elif user_input == "9":
        user_id = input("Enter id of user: ")
        if user_id.isnumeric():
            column_name = input(
                f"Enter the column you want to edit. Please make sure column is with in {COLUMNS}: "
            )
            if column_name in COLUMNS:
                column_value = input(f"Enter the value of {column_name}: ")
                update_user_by_id(con, user_id, column_name, column_value)


    

     else:
        exit()


main()
