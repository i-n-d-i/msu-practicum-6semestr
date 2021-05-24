import os
import networkx as nx
from .shortest_paths import read_graph, dist_matrix, write_matrix
import numpy as np


def test_read_graph():
    f = open('../graph.txt', 'r')
    graph = read_graph(f)
    f.close()
    assert len(graph.nodes()) > 0
    assert len(graph.edges()) > 0
    assert nx.is_weighted(graph)


def test_dist_matrix():
    graph = nx.gnc_graph(0)
    edges = np.array([(1, 0, 17), (2, 0, 2), (3, 0, 7), (3, 2, 7), (4, 0, 19), (4, 2, 15), (5, 0, 19), (5, 2, 13),
                      (6, 0, 13), (6, 2, 10), (6, 3, 11), (7, 0, 20), (8, 0, 14), (8, 2, 10), (8, 3, 17), (9, 0, 6)])
    graph.add_weighted_edges_from(edges)
    dist_true = nx.floyd_warshall_numpy(graph)
    dist_check = dist_matrix(graph)
    for i in range(10):
        for j in range(10):
            assert dist_true[i][j] == dist_check[i][j]


def test_write_matrix():
    f = open('../matrix.txt', 'w+')
    graph = nx.gnc_graph(0)
    edges = np.array([(1, 0, 17), (2, 0, 2), (3, 0, 7), (3, 2, 7), (4, 0, 19), (4, 2, 15), (5, 0, 19), (5, 2, 13),
                      (6, 0, 13), (6, 2, 10), (6, 3, 11), (7, 0, 20), (8, 0, 14), (8, 2, 10), (8, 3, 17), (9, 0, 6)])
    graph.add_weighted_edges_from(edges)
    matrix = dist_matrix(graph)
    write_matrix(matrix, f)
    f.close()
    assert os.path.getsize('../matrix.txt') > 0


def main():
    test_read_graph()
    test_dist_matrix()
    test_write_matrix()


if __name__ == "__main__":
    main()
