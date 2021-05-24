import networkx as nx


def read_graph(input):
    G = nx.gnc_graph(0)
    edges = []
    for line in input:
        edge = tuple(map(int, line[1:len(line) - 2].split(', ')))
        edges.append(edge)
    G.add_weighted_edges_from(edges)

    return G


def dist_matrix(G):
    dist = nx.floyd_warshall_numpy(G)
    return dist


def write_matrix(dist, output):
    print(dist, file=output)
