import os
from .graph_generator import generator, write_graph


def test_generator():
    graph = generator(15)
    assert(len(graph.nodes()) == 15)


def test_generator_2():
    graph = generator(30)
    for e in graph.edges():
        assert e[0] >= 0
        assert e[1] >= 0


def test_generator_3():
    graph = generator(15)
    for e in graph.edges():
        assert graph[e[0]][e[1]]['weight'] >= 1


def test_write_graph():
    graph = generator(15)
    f = open('../graph.txt', 'w+')
    write_graph(graph, f)
    f.close()
    assert os.path.getsize('../graph.txt') > 0


def main():
    test_generator()
    test_generator_2()
    test_generator_3()
    test_write_graph()


if __name__ == "__main__":
    main()
