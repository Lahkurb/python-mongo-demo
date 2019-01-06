from pymongo import MongoClient
client = MongoClient('mongodb://mongo-0.mongo.sample-app.svc.cluster.local,mongo-1.mongo.sample-app.svc.cluster.local.mongo,mongo-2.mongo.sample-app.svc.cluster.local:27017/')

# data base name : 'test-database-1'
mydb = client['test-database-1']

import datetime

myrecord = {
        "author": "Duke",
        "title" : "PyMongo 101",
        "tags" : ["MongoDB", "PyMongo", "Tutorial"],
        "date" : datetime.datetime.utcnow()
        }

record_id = mydb.mytable.insert(myrecord)

print('###########MongoDB Demo######')
print('Inserted record: ',record_id)
print('table_name',mydb.collection_names())

# find all documents
results = mydb.mytable.find()
 
print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
 
# display documents from collection
for record in results:
    # print out the document
    print(record['author'] + ',',record['title'])
 
    print()

print('###########MongoDB Demo######')
