"""
Imports
"""
import os
import pymongo
if os.path.exists("env.py"):
    # if in a local development the env.py file will be loaded
    # otherwise on a deployed site it would use MongoDB variables
    import env


# All python constants are written in all capitals, with underscores
# seperating any words this is standard practice for python
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


# Create a function to connect to the database
def mongo_connect(url):
    """
    Connects to the mongoDB
    """
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        # the placeholder %s is for the error message
        print("Could not connect to MongoDB %s") % e


def show_menu():
    """
    prints the menu options in the terminal,
    this is the full CRUD functionality
    """
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit the menu")

    option = input("Enter option: ")
    return option


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


# conn variable - stores the URI link for the MongoDB
conn = mongo_connect(MONGO_URI)

# coll variable - stores the database & collection
coll = conn[DATABASE][COLLECTION]

main_loop()