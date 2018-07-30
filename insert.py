import pymongo
import pprint
from str2dict import convert

client = pymongo.MongoClient("mongodb+srv://Shantom:134558@paradise-39qvg.mongodb.net/test?retryWrites=true")
db = client.test
coll = db.test


formulas=[]
with open('配方.txt') as file:
      for line in file:
            formulas.append(convert(line))


coll.insert_many(formulas)



