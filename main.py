import pymongo
import pprint
client = pymongo.MongoClient("mongodb+srv://Shantom:134558@paradise-39qvg.mongodb.net/test?retryWrites=true")
db = client.test
coll = db.test

# for data in coll.find({'product':'花圃'}):
#     print(data)

post={'product':'石材',
      'tool':'碎石机01',
      'ingredients':[{'name':'岩石',
                      'count':111}]}
# coll.insert_one(post)
pprint.pprint(post)
