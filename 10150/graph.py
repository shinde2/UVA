from collections import deque


class Edge:

    def __init__(self, y, weight=0):
        self.y = y
        self.weight = weight


class Graph:

    NVERTICES = 10

    def __init__(self, directed=False):

        self.nvertices = Graph.NVERTICES+1
        self.nedges = 0
        self.degree = [0] * (Graph.NVERTICES+1)
        self.edges = [None] * (Graph.NVERTICES+1)
        self.directed = directed

    def insert_edge(self, x, y, directed=True):

        edge = Edge(y)

        if self.edges[x]:
            self.edges[x].append(edge)
        else:
            self.edges[x] = [edge]

        if directed:
            self.insert_edge(y, x, directed=False)
        else:
            self.degree[x] += 1

    def has_edge(self, x, y):

        return y in self.edges[x]

    def read_graph(self, edges):

        for u, v in edges: self.insert_edge(u, v)

    def print_graph(self):

        for i, edges in enumerate(self.edges[1:]):
            print(f"-"*40)
            print(f"From {i+1} to: ")
            for edge in edges:
                print(f"{edge.y}")


def parent_level(parent, n):

    if not parent[n]:
        return 0
    else:
        return 1 + parent_level(parent, parent[n])


def bfs(g, start):

    q = deque()
    discovered = [False] * (g.NVERTICES+1)
    processed = [False] * (g.NVERTICES+1)
    parent = [None] * (g.NVERTICES+1)

    discovered[start] = True
    q.append(start)

    while q:
        head = q.popleft()
        for edge in g.edges[head]:
            if not discovered[edge.y]:
                discovered[edge.y] = True
                parent[edge.y] = head
                q.append(edge.y)
        processed[head] = 1
        #print(head)

    return parent


def main():

    edges = [(1, 2), (1, 3),
             (2, 3), (2, 5), (2, 4),
             (4, 3)
             ]

    g = Graph()
    g.read_graph(edges)
    #g.print_graph()

    parent = bfs(g, 3)
    level = parent_level(parent, 5)

    print(level)


if __name__ == '__main__':
    main()
