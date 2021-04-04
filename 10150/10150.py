from graph import Graph


def shortest_path(g, x):

    parents = [None] * (g.NVERTICES+1)
    intree = [False] * (g.NVERTICES+1)
    shortest = [float("Inf")] * (g.NVERTICES+1)
    shortest[x] = 0

    while not intree[x]:
        intree[x] = True
        for edge in g.edges[x]:
            if shortest[x] + 1 < shortest[edge.y]:
                shortest[edge.y] = shortest[x] + 1
                parents[edge.y] = x

        mini = 1
        val = float("inf")
        for v in range(1, g.NVERTICES+1):
            if not intree[v] and shortest[v] < val:
                mini = v
                val = shortest[v]
        x = mini

    return parents


def is_doublet(word1, word2):

    if len(word1) != len(word2):
        return False
    else:
        count = 0
        for i, w1 in enumerate(word1):
            if count > 1:
                return False
            if w1 != word2[i]:
                count += 1
        else:
            if count == 1:
                return True
            else:
                return False


def trace(parents, v, dictionary):

    if not parents[v]:
        for k, val in dictionary.items():
            if val == v:
                print(k)
    else:
        trace(parents, parents[v], dictionary)
        for k, val in dictionary.items():
            if val == v:
                print(k)


def main():

    g = Graph()

    #g.insert_edge(1, 2)
    #g.insert_edge(2, 3)
    #g.insert_edge(2, 5)
    #g.insert_edge(3, 4)
    #g.insert_edge(3, 5)
    #parents = shortest_path(g, 1)
    #print(is_doublet("booster", "raoster"))

    dictionary = {
        "booster": 1,
        "rooster": 2,
        "roaster": 3,
        "coasted": 4,
        "roasted": 5,
        "coastal": 6,
        "postal": 7

    }
    tests = [["booster", "roasted"], ["coastal", "postal"]]
    g.NVERTICES = len(dictionary.keys())
    words = list(dictionary.keys())

    for i, word1 in enumerate(words):
        for word2 in words[i+1:]:
            if is_doublet(word1, word2) and not g.has_edge(dictionary.get(word1), dictionary.get(word2)):
                g.insert_edge(dictionary.get(word1), dictionary.get(word2))

    if g.is_empty():
        print("No solution")
    else:
        for u, v in tests:
            parents = shortest_path(g, dictionary.get(u))
            if parents[dictionary.get(v)]:
                trace(parents, dictionary.get(v), dictionary)
            else:
                print("No solution")


if __name__ == '__main__':
    main()
