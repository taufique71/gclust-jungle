import networkx as nx
import scipy as sp
from scipy import io as spio
import sys
import math
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

if __name__=="__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    emb_dim = int(sys.argv[3])
    nrow = int(sys.argv[4])
    
    tokens = input_file.split(".")
    if tokens[-1] == "spec-emb":
        # nrow = 0
        # with open(input_file) as fp:
            # for _ in fp:
                # nrow += 1
        # df = pd.read_csv()
        # x = np.fromfile(input_file, np.float32).reshape(nrow, 32)
        X = np.fromfile(input_file, sep=" ").reshape(nrow, emb_dim)
        k = math.ceil(math.sqrt(nrow));
        kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
        with open(output_file, 'w') as fp:
            for x in kmeans.labels_:
                fp.write(str(x))
                fp.write("\n")
            fp.close()
        print(X.shape)
    if tokens[-1] == "verse-emb":
        X = np.fromfile(input_file, np.float32).reshape(nrow, emb_dim)
        k = math.ceil(math.sqrt(nrow));
        kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
        with open(output_file, 'w') as fp:
            for x in kmeans.labels_:
                fp.write(str(x))
                fp.write("\n")
            fp.close()
        print(X.shape)
