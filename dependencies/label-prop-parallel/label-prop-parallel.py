import networkx as nx
import networkit as nk
import scipy as sp
from scipy import io as spio
import sys
import math
import os

if __name__=="__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    omp_number_of_threads = int(os.environ["OMP_NUM_THREADS"])
    nk.setNumberOfThreads(omp_number_of_threads);

    edgeListReader = nk.graphio.EdgeListReader(" ",0)
    G = edgeListReader.read(input_file)

    communities = nk.community.detectCommunities(G, algo=nk.community.PLP(G))
    nk.community.writeCommunities(communities, output_file)
    
