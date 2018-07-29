import pymongo
import pprint
from str2dict import convert

client = pymongo.MongoClient("mongodb+srv://Shantom:134558@paradise-39qvg.mongodb.net/test?retryWrites=true")
db = client.test
coll = db.test

# for data in coll.find({'product':'花圃'}):
#     print(data)

formulas=[]
with open('花圃配方.txt') as file:
      for line in file:
            formulas.append(convert(line))


coll.insert_many(formulas)
