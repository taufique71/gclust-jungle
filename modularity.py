import os
from pathlib import Path
import networkx as nx
import scipy as sp
from scipy import io as spio
import json
import subprocess
import time
import sys
import clusim
import networkx.algorithms.community as nx_comm
from networkx.algorithms.community.community_utils import is_partition
import re

def read_graph(config):
    filename = config["location"] + "/" + config["filename"] + "." + "mtx"
    M = spio.mmread(filename);
    G = nx.from_scipy_sparse_matrix(M)
    return G

def read_infomap_partition(filename):
    p_dict = {}

    try:
        f = open(filename, 'r')
    except OSError as e:
        # print('open() failed', e)
        return p_dict.values()

    with open(filename, 'r') as f:
        for line in f:
            if line[0] != '#':
                splitted_line = line.split(" ")
                n = int(splitted_line[0])
                p = int(splitted_line[1])
                n = n
                p = p
                if p in p_dict.keys():
                    p_dict[p].add(n)
                else:
                    p_dict[p] = set([])
                    p_dict[p].add(n)
    p_list = p_dict.values()
    return p_list

def read_louvain_partition(filename):
    p_dict = {}
    try:
        f = open(filename, 'r')
    except OSError as e:
        # print('open() failed', e)
        return p_dict.values()

    n = 0
    with open(filename, 'r') as f:
        for line in f:
            if line[0].isdigit():
                p = int(line)
                if p in p_dict.keys():
                    p_dict[p].add(n)
                else:
                    p_dict[p] = set([])
                    p_dict[p].add(n)
                n = n + 1
            else:
                pass
    p_list = p_dict.values()
    return p_list

def read_mcl_partition(filename):
    p_dict = {}
    try:
        f = open(filename, 'r')
    except OSError as e:
        # print('open() failed', e)
        return p_dict.values()
    with open(filename, 'r') as f:
        p = 0
        for line in f:
            if p not in p_dict.keys():
                p_dict[p] = set([])
            splitted_line = re.split('\s+', line)
            for tok in splitted_line:
                tok = tok.strip()
                if tok.isdigit():
                    n = int(tok)
                    p_dict[p].add(n)
            p = p + 1
    p_list = p_dict.values()
    return p_list

def measure_modularity(G, p):
    mod = nx_comm.modularity(G, p)
    return mod

if __name__=="__main__":
    f = open('config.json',)
    config = json.load(f)

    # Determine which dataset to use
    # Always use dataset specified in config
    dset = config["dataset"]
    
    # Determine which algorithms to run
    algset = []
    if len(sys.argv) < 2:
        # If no algorithm is specified then read from config file
        algset = config["algorithms"]
    else:
        # If algorithms are specified then use the specified algorithms
        i = 1
        while i < len(sys.argv):
            algset.append(sys.argv[i])
            i = i+1

    for item in dset:
        # G = None
        G = read_graph(item)
        for alg in algset:
            filename = item["location"] + "/" + item["filename"] + "." + alg
            p_list = []
            if alg == "infomap":
                # change default filename
                filename = item["location"] + "/" + item["filename"] + "." + "clu"
                p_list = read_infomap_partition(filename)
            elif alg == "infomap-parallel":
                # change default filename
                filename = item["location"] + "/" + item["filename"] + "." + "infomap-parallel" + "." + "clu"
                p_list = read_infomap_partition(filename)
            elif alg == "louvain":
                p_list = read_louvain_partition(filename)
            elif alg == "spectral-modularity":
                p_list = read_louvain_partition(filename)
            elif alg == "louvain-parallel":
                p_list = read_louvain_partition(filename)
            elif alg == "label-prop":
                p_list = read_louvain_partition(filename)
            elif alg == "label-prop-parallel":
                p_list = read_louvain_partition(filename)
            elif alg == "mcl":
                p_list = read_mcl_partition(filename)
            elif alg == "kernighan-lin":
                p_list = read_mcl_partition(filename)

            # print(is_partition(G, p_list))
            # x = set([])
            # for p in p_list:
                # x = x.union(set(p))
            # y = set(G.nodes)
            # print(y.difference(x))
            # # print(x)
            # # print(y)

            # if len(p_list) > 0:
                # # Read graph only if there is a non empty partition found
                # G = read_graph(item)

            if is_partition(G, p_list):
                Q = measure_modularity(G, p_list)
                print(item["name"] + "," + alg + "," + "modularity" + "," + str(Q))
            else:
                print(item["name"] + "," + alg + "," + "modularity" + "," + "-100")
