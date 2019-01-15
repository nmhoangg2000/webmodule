from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_database()
rivers = db["river"]

africa = []
america = []
river_list = rivers.find()
for p in river_list:
    if p["continent"] == "Africa":
        africa.append(p["name"])
    if p["continent"] == "S. America" and p["length"] < 1000:
        america.append(p["name"])
print(africa)
print(america)

client.close()