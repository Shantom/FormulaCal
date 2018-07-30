import pymongo
import pprint
from str2dict import convert
from topology import Graph
from algorithms.queues import queue
import math

client = pymongo.MongoClient("mongodb+srv://Shantom:134558@paradise-39qvg.mongodb.net/test?retryWrites=true")
db = client.test
coll = db.test

g = Graph('花圃', 1)
q = queue.ArrayQueue()
q.enqueue(g.product)

basicIngs=[]
while not q.is_empty():
    parent = q.dequeue()

    doc = coll.find_one({'product':parent.name})
    if not doc: # final ings
        basicIngs.append(parent)
        continue
    ings = doc['ingredients']
    count = int(doc['count'])
    tool = doc['tool']

    for item in ings:
        weight = math.ceil(parent.wt / count) * item['count']
        node = g.add_node(item['name'], weight)
        g.add_edge(item['name'], parent.name, weight, tool)
        if node not in q._array:
            q.enqueue(node)

steps=[]
for node in g.nodes:
    step = [edge for edge in g.edges if node == edge.nt]
    
    if step:
        product = step[0].nt
        tool = step[0].tool
        ings = []
        for item in step:
            ing = '{0}个{1}'.format(item.wt, item.nf.name)
            ings.append(ing)
        ings = ', '.join(ings)

        step = '工具：{0}, 成品：{1}, 原料：{2}'.format(tool, product, ings)
   
        steps.append(step)

steps=steps[::-1]
pprint.pprint(steps)


print(basicIngs)
