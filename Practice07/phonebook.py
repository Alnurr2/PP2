import psycopg2
import csv
from config import load_config


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
def insert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur = conn.cursor()
    
    cur.execute(
        "INSERT INTO phonebook (phone,phone_owner) VALUES (%s, %s)",
        (phone, name)
    )

    conn.commit()
    print("Contact added.")
    cur.close()


#Updating contact
def update_contact():
    name = input("Enter name to update: ")
    phone = input("New phone: ")


    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE name = %s",
        (phone, name)
    )

    conn.commit()

#Searching
def search_contact():
    keyword = input("Search name: ")


    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        (f"%{keyword}%",)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.commit()

#Deleting
def delete_contact():
    name = input("Enter name to delete: ")

    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE name = %s",
        (name,)
    )

#Show all
def showall():
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close() 


def menu():
    while True:
        print("------------Phonebook-----------")
        print("1.Show the contacts")
        print("2.Add contact")
        print("3.Deleting contact")
        print("0.Exit")


        choice = input("Choose:")

        if choice == "1":
         showall()
        elif choice == "2":
         insert_contact()
        elif choice == "3":
         delete_contact()
        elif choice == "0":
         conn.close()
         break

if __name__=="__main__":
   menu()
