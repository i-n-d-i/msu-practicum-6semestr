import networkx as nx
import random


def generator(vertices):
    graph = nx.gnc_graph(vertices)
    weights = []
    for i in range(len(graph.edges())):
        weights.append(random.randint(1, 20))

    counter = 0
    for e in graph.edges():
        graph[e[0]][e[1]]['weight'] = weights[counter]
        counter += 1

    return graph


def write_graph(graph, f):
    # print(graph.edges(), file=f)
    for e in graph.edges():
        print(e + tuple(map(int, str(graph[e[0]][e[1]]['weight']).split(', '))), file=f)
