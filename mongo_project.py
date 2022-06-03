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


def get_record():
    """
    search function - use names for finding data
    """
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    # searches the database for first & last name (converted to lowercase)
    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})

    # message shown if error accessing the database
    except:
        print("Error accessing the database")

    # if no document is returned, record looking for not found
    # an empty cursor object is returned
    if not doc:
        print("")
        print("Error! No results found.")

    return doc


def add_record():
    """
    add record function
    Prompts the user to enter the following information
    """
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")


# new_doc variable - dictionary with info entered by user
# use .lower() on first & last names to store them in lower case
# (makes it easier to find items later)
    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }

    # insert the new_doc variable to the DB
    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")

    # if data can't be inserted show error message
    except:
        print("Error accessing the database")


def find_record():
    """
    find the records
    k = key, v = value
    checks that the key isn't the _id as we want to kept that secret
    """
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    """
    edit a record
    checks that the key is not _id as we don't want to change this
    This will then display the current value for the key for users to see
    before editing. If the input is empty we will keep the original value,
    without updating the field
    """
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def delete_record():
    """
    find a record using first and last name,
    confirm if the user wants to delete
    """
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.delete_one(doc)
                print("Document deleted!")
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")


def main_loop():
    """
    main loop for options
    """
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
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
