import argparse
from graph_generator.graph_generator import generator, write_graph
from shortest_paths.shortest_paths import read_graph, dist_matrix, write_matrix


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    parser_a = subparsers.add_parser('graph_generator')
    parser_a.add_argument('vertices', type=int, help='count of graph vertices')
    parser_a.add_argument('outdir', type=str, help='output file for graph')

    parser_b = subparsers.add_parser('shortest_paths')
    parser_b.add_argument('indir', type=str, help='input file with graph')
    parser_b.add_argument('outdir', type=str, help='output file with matrix of shortest paths')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.command == 'graph_generator':
        f = open(args.outdir, 'w')
        graph = generator(args.vertices)
        write_graph(graph, f)
        f.close()

    if args.command == 'shortest_paths':
        indir = open(args.indir, 'r')
        outdir = open(args.outdir, 'w')

        graph = read_graph(indir)
        matrix = dist_matrix(graph)
        write_matrix(matrix, outdir)

        indir.close()
        outdir.close()


if __name__ == "__main__":
    main()
