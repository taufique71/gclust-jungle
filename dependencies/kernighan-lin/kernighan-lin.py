import networkx as nx
import scipy as sp
from scipy import io as spio
import sys
import math

if __name__=="__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    M = spio.mmread(input_file);
    G = nx.from_scipy_sparse_matrix(M)
    k = int(math.sqrt(G.number_of_nodes()))

    (p1, p2) = nx.algorithms.community.kernighan_lin.kernighan_lin_bisection(G)

    G1 = G.subgraph(p1)
    G2 = G.subgraph(p2)

    del G

    clusters1 = [G1, G2]
    while len(clusters1) < k:
        clusters2 = []
        for i in range(len(clusters1)):
            (p1, p2) = nx.algorithms.community.kernighan_lin.kernighan_lin_bisection(clusters1[i])
            clusters2.append(clusters1[i].subgraph(p1))
            clusters2.append(clusters1[i].subgraph(p2))
        clusters1 = list(clusters2)


    with open(output_file, "w") as f:
        for c in clusters1:
            content = ""
            for n in c.nodes:
                content += str(n) + " "
            content += "\n"
            f.write(content)
        f.close()
