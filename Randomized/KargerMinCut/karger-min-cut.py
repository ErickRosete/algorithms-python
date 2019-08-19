class Graph:
    def __init__(self, vertices = []):
        self.vertices = vertices
    
    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
    
    def add_edge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            return False
        u.add_neighbor(v)
        v.add_neighbor(u)
        return True

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex.name, " -> ", list(map(lambda v: v.name, vertex.neighbors)))
    
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)

graph = Graph()
vertices = list(range(0, 5))
vertices = list(map(lambda v: Vertex(v), vertices))
for v in vertices:
    graph.add_vertex(v)
graph.add_edge(vertices[0], vertices[2])
graph.add_edge(vertices[0], vertices[4])
graph.add_edge(vertices[0], vertices[3])
graph.add_edge(vertices[2], vertices[3])
graph.add_edge(vertices[3], vertices[1])
graph.add_edge(vertices[3], vertices[4])
graph.print_graph()

graph2 = {
    0: [2, 4, 3],
    1: [],
    2: [3],
    3: [1],
    4: [2],
}