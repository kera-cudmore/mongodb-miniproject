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
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        # the placeholder %s is for the error message
        print("Could not connect to MongoDB %s") % e


# conn variable - stores the URI link for the MongoDB
conn = mongo_connect(MONGO_URI)

# coll variable - stores the database & collection
coll = conn[DATABASE][COLLECTION]

# INSERTING A SINGLE DOCUMENT
# both the key & value to be wrapped in quotes
# This line would usually be split to be PEP8 compliant
# new_doc = {"first": "douglas", "last": "adams", "dob": "11/03/1952",
# "hair_color": "grey", "occupation": "writer", "nationality": "british"}

# Inserts single document (a dictionary of key value pairs)
#  into the celebrities collection
# coll.insert_one(new_doc)

# INSERTING MANY DOCUMENTS
# This is done by inserting an array of dictionaries
# new_docs = [{
#     "first": "terry",
#     "last": "pratchett",
#     "dob": "28/04/1948",
#     "gender": "m",
#     "hair_color": "not much",
#     "occupation": "writer",
#     "nationality": "british"
# }, {
#     "first": "george",
#     "last": "rr martin",
#     "dob": "20/09/1948",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation": "writer",
#     "nationality": "american"
# }]


# # Inserts many documents
# coll.insert_many(new_docs)


# Prints all documents by finding and then printing each one
# documents = coll.find()


# Finding specific data
# put the key/value pair in a dictionary for the specific data that we want
# this searches the database for all entries where the first name is douglas
# documents = coll.find({"first": "douglas"})


# DELETING DATA - delete_one()
# to remove multiple data with same key we use .delete_many()
# this replaces .remove()
# coll.delete_one({"first": "douglas"})
# documents = coll.find()


# UPDATING INFORMATION ON THE DATABASE - one
# the first argument is the search parameters - nationality
# the second argument uses $set keyword - as we want to set new data into the
#  document
# coll.update_one({"nationality": "american"},
#                 {"$set": {"hair_color": "maroon"}})
# documents = coll.find({"nationality": "american"})

# UPDATING INFORMATION ON THE DATABASE - many
coll.update_many({"nationality": "american"},
                 {"$set": {"hair_color": "maroon"}})

documents = coll.find({"nationality": "american"})

for doc in documents:
    print(doc)
