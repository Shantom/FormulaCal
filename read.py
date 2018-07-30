import pymongo
import pprint
from str2dict import convert
from topology import Graph
from algorithms.queues import queue

client = pymongo.MongoClient("mongodb+srv://Shantom:134558@paradise-39qvg.mongodb.net/test?retryWrites=true")
db = client.test
coll = db.test

g = Graph('花圃', 1)
q = queue.ArrayQueue()
q.enqueue(g.product)

while not q.is_empty():
    parent = q.dequeue()

    doc = coll.find_one({'product':parent.name})
    if not doc: # final ings
        continue
    ings = doc['ingredients']
    count = int(doc['count'])
    tool = doc['tool']

    for item in ings:
        weight = parent.wt // count * item['count']
        node = g.add_node(item['name'], weight)
        g.add_edge(item['name'], parent.name, weight, tool)
        if node not in q._array:
            q.enqueue(node)

for edge in g.edges:
    print(edge)
