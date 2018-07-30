from graph import DirectedGraph

class Graph(DirectedGraph):
    def __init__(self, product = None, count = 1):
        super(Graph,self).__init__()
        if product:
            self.product = self.add_node(product, 1)
        
    def setProduct(self, product):
        self.product = product

    def process(self):
        pass

    

# g = Graph()
# g.add_node('1')
# g.add_node('2')
# g.add_edge('1','2',2)


# print(g.edges)
# print(g.nodes)
