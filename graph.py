"""
These are classes to represent a Graph and its elements.
It can be shared across graph algorithms.
"""

class Node(object):
    def __init__(self, name, weight = 0):
        self.name = name
        self.wt = weight

    @staticmethod
    def get_name(obj):
        if isinstance(obj, Node):
            return obj.name
        elif isinstance(obj, str):
            return obj
        return''
    
    def __eq__(self, obj):
        return self.name == self.get_name(obj)

    def __repr__(self):
        return '%d个'%self.wt+self.name
    
    def __hash__(self):
        return hash(self.name)

    def __ne__(self, obj):
        return self.name != self.get_name(obj)

    def __lt__(self, obj):
        return self.name < self.get_name(obj)

    def __le__(self, obj):
        return self.name <= self.get_name(obj)

    def __gt__(self, obj):
        return self.name > self.get_name(obj)

    def __ge__(self, obj):
        return self.name >= self.get_name(obj)

    def __bool__(self):
        return self.name

class DirectedEdge(object):
    def __init__(self, node_from, node_to, weight = 0, tool = None):
        self.nf = node_from
        self.nt = node_to
        self.wt = weight
        self.tool = tool

    def __eq__(self, obj):
        if isinstance(obj, DirectedEdge):
            return obj.nf == self.nf and obj.nt == self.nt
        return False
    
    def __repr__(self):
        return '({0}个{1} -> {2}), {3}'.format(self.wt, self.nf.name, self.nt, self.tool)

    def setWeight(self, weight):
        self.wt = weight

class DirectedGraph(object):
    def __init__(self, load_dict={}):
        self.nodes = []
        self.edges = []
        self.adjmt = {}

        if load_dict and type(load_dict) == dict:
            for v in load_dict:
                node_from = self.add_node(v)
                self.adjmt[node_from] = []
                for w in load_dict[v]:
                    node_to = self.add_node(w)
                    self.adjmt[node_from].append(node_to)
                    self.add_edge(v, w, 0)

    def add_node(self, node_name, weight = 0):
        try:
            id = self.nodes.index(node_name)
            self.nodes[id].wt += weight
            return self.nodes[id]
        except ValueError:
            node = Node(node_name, weight)
            self.nodes.append(node)
            return node
    
    def add_edge(self, node_name_from, node_name_to, weight, tool):
        try:
            node_from = self.nodes[self.nodes.index(node_name_from)]
            node_to = self.nodes[self.nodes.index(node_name_to)]
            self.edges.append(DirectedEdge(node_from, node_to, weight, tool))
        except ValueError:
            pass

class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = {}

        # To store transitive closure
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    # function to add an edge to graph
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
            
#g = Graph(4)
#g.add_edge(0, 1)
#g.add_edge(0, 2)
#g.add_edge(1, 2)
#g.add_edge(2, 0)
#g.add_edge(2, 3)
#g.add_edge(3, 3)
