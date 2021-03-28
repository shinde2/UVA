from pprint import pprint as print
from graph import Graph
from graph import bfs


def parent_level(parent, n):

    if not parent[n]:
        return 0, n
    else:
        v, n = parent_level(parent, parent[n])
        return v+1, n


def erdos(authors, papers, outputs):

    Graph.NVERTICES = len(authors.keys())
    g = Graph()
    index = authors.get("Erdos, P.")
    edges = list()

    for p, auths in papers.items():
        a_i = [authors.get(a) for a in auths]
        for _i, i in enumerate(a_i):
            for _j, j in enumerate(a_i[_i+1:]):
                edges.append((i, j))

    g.read_graph(edges)
    parent = bfs(g, index)

    for o in outputs:
        i = authors.get(o)
        n, idx = parent_level(parent, i)
        if idx == index:
            print(f"{o} {n}")
        else:
            print(f"{o} infinity")


def prepare_scenario(scenarios):

    prepared = list()

    for scenario in scenarios:
        i = 0
        authors = dict()
        papers = dict()
        inputs = scenario[0]
        for input in inputs:
            names, paper = input.split(":")
            ns = names.split(".,")
            names = [n+"." for n in ns[0:len(ns)-1]]
            names.append(ns[len(ns)-1])
            for name in names:
                papers.setdefault(paper.strip(), []).append(name.strip())
                if name not in authors.keys():
                    i += 1
                    authors.setdefault(name.strip(), i)
        prepared.append([authors, papers, scenario[1]])

    i = 1
    for prep in prepared:
        print(f'Scenario {i}')
        erdos(*prep)
        i += 1


def main():

    scenarios = []

    with open("tests.txt") as f:
        lines = f.readlines()

    index = 1
    while index < len(lines):
        i, o = lines[index].rstrip().split()
        i = int(i)
        o = int(o)
        input = []
        output = []
        for _i in range(index+1, index+i+1):
            input.append(lines[_i].rstrip())
        for _o in range(index+i+1, index+i+o+1):
            output.append(lines[_o].rstrip())
        scenarios.append([input, output])
        index += (i+o+1)

    prepare_scenario(scenarios)


if __name__ == '__main__':
    main()
