import os
import networkx as nx
import scipy as sp
from scipy import io as spio
import json


if __name__=="__main__":

    f = open('config.json',)
    config = json.load(f)
    ds_config = config["dataset"]
    # print(len(ds_config));
    for dc in ds_config:
        if(dc["conversion"] and dc["conversion"]["convert"] == "yes"):
            G = None
            if (dc["conversion"]["from"] == "mtx"):
                input_file = dc["location"] + "/" + dc["filename"] + "." + dc["conversion"]["from"]
                print("Reading:", input_file)
                M = spio.mmread(input_file);
                G = nx.from_scipy_sparse_matrix(M)
            for target in dc["conversion"]["to"]:
                output_file = dc["location"] + "/" + dc["filename"] + "." + target
                print("Writing:", output_file)
                if(target == "edgelist"):
                    if( nx.is_weighted(G) ):
                        nx.write_weighted_edgelist(G, output_file)
                    else:
                        nx.write_edgelist(G, output_file, data=False)
                elif(target == "pajek"):
                    nx.write_pajek(G, output_file)


    # rootDir = 'data'

    # for dirName, subdirList, fileList in os.walk(rootDir):
        # # print('Found directory: %s' % dirName)
        # for fname in fileList:
            # if fname.endswith(".mtx"):
                # dirs = dirName.split("/")
                # trimmedFname = fname[:-4]
                # # print(dirs[-1], trimmedFname);
                # if dirs[-1] == trimmedFname:
                    # mtxFname = dirName + "/" + fname
                    # print('\t%s' % mtxFname)
                    # edgelistFname = mtxFname[:-3] + "edgelist"
                    # M = spio.mmread(mtxFname);
                    # G = nx.from_scipy_sparse_matrix(M)
                    # nx.write_edgelist(G, edgelistFname)
                    # print('\t%s' % edgelistFname)
