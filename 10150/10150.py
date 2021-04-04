from graph import Graph


def shortest_path(g, x):

    parents = [None] * (g.NVERTICES+1)
    intree = [False] * (g.NVERTICES+1)
    shortest = [float("Inf")] * (g.NVERTICES+1)
    shortest[x] = 1

    while not intree[x]:
        for edge in g.edges[x]:
            if shortest[x] + 1 < shortest[edge.y]:
                shortest[edge.y] = shortest[x] + 1
        mini = 0
        for i, val in enumerate(shortest[1:], start=1):
            if not intree[i] and val < shortest[mini]:
                mini = i
        intree[x] = True
        parents[mini] = x
        x = mini

    return parents


def main():

    g = Graph()
    g.NVERTICES = 5

    g.insert_edge(1, 2)
    g.insert_edge(2, 3)
    g.insert_edge(2, 5)
    g.insert_edge(3, 4)
    g.insert_edge(3, 5)
    parents = shortest_path(g, 1)
    print(parents)


if __name__ == '__main__':
    main()