import psycopg2
import csv
from config import load_config
import re



conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="Qwerty5656"
)
#Creating the PhoneBook Table
def create_tables():
    command = """
CREATE TABLE IF NOT EXIST phonebook (
               phone_id SERIAL PRIMARY KEY,
               phone VARCHAR(16) NOT NULL,
               phone_owner VARCHAR(255) NOT NULL
);
""" 
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()
#Adding Contact function
def upsert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur = conn.cursor()
    
    cur.execute(
       "CALL upsert_contact(%s,%s);",(phone, name)
    )

    conn.commit()
    print("Contact added.")
    cur.close()

# PAGINATION
def paginate_contact():
    limit = input("Enter limit: ")
    offset = input("Enter offset: ")


    cur = conn.cursor()
    
    cur.execute(
       "SELECT get_contacts_paginated(%s,%s);",(limit, offset)
    )


    rows = cur.fetchall()
    for row in rows:
       print(row)
    cur.close()

#Searching
def search_contact():
    keyword = input("Search name: ")


    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE phone_owner ILIKE %s",
        (f"%{keyword}%",)
    )


    rows = cur.fetchall()
    for row in rows:
        print(row)
    if len(rows) == 0:
       print("Didnt find any contact with that name.")
    conn.commit()
    cur.close()

#Deleting
def delete_contact():
    value = input("Enter name or phone to delete: ")
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s);", (value,))
    conn.commit()
    print("Contact has been deleted.")
    cur.close()

#Show all
def showall():
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    if len(rows) == 0:
       print("No contacts yet.")
    for row in rows:
        print(row)
    cur.close() 

#Exporting to csv

def add_several_contacts():
    n = int(input("Number of contacts: ")) 

    names = []
    phones = []
    pattern = r"^\+7\d{10}$"

    for _ in range(n):
        name = input("Name: ")

        while True:
            phone = input("Phone: ")
            if re.fullmatch(pattern, phone):
                break
            else:
                print("Invalid phone, try again")


        names.append(name)
        phones.append(phone)

    cur = conn.cursor()
    cur.execute(
        "CALL insert_contacts(%s, %s)",
        (phones, names)
    )

    conn.commit()
    cur.close()

#Importing from csv
def importing_to_csv(file):
    cur = conn.cursor()


    with open(file, 'r', newline='') as f:
        import csv
        reader= csv.reader(f)
        next(reader)
        for row in reader:
           if not row or len(row) < 2:
            continue
           cur.execute("INSERT INTO phonebook (phone,phone_owner) VALUES (%s,%s)", row)

    conn.commit()
    cur.close()


def menu():
    while True:
        print("------------Phonebook-----------")
        print("1.Show the contacts")
        print("2.Upsert the contact")
        print("3.Deleting contact")
        print("5.Search contact")
        print("6.Add several contacts")
        print("7.import from csv")
        print("8.Paginate table")
        print("0.Exit")


        choice = input("Choose:")

        if choice == "1":
         showall()
        elif choice == "2":
         upsert_contact()
        elif choice == "3":
         delete_contact()
        elif choice == "5":
         search_contact()
        elif choice == "6":
         add_several_contacts()
        elif choice == "7":
         importing_to_csv("import.csv")
        elif choice == "8":
           paginate_contact()
        elif choice == "0":
         conn.close()
         break

if __name__=="__main__":
   menu()
