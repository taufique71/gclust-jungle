import os
from pathlib import Path
import networkx as nx
import scipy as sp
from scipy import io as spio
import json
import subprocess

def mtx_to_edgelist(input_file, output_file):
    print("mtx_to_edgelist")
    M = spio.mmread(input_file);
    G = nx.from_scipy_sparse_matrix(M)
    print("Read:", input_file)
    nx.write_weighted_edgelist(G, output_file)
    print("Written:", output_file)

def mtx_to_pajek(input_file, output_file):
    print("mtx_to_pajek")
    M = spio.mmread(input_file);
    G = nx.from_scipy_sparse_matrix(M)
    print("Read:", input_file)
    nx.write_pajek(G, output_file)
    print("Written:", output_file)

def edgelist_to_bcsr(input_file, output_file):
    print("edgelist_to_bcsr")
    # python convert.py --format weighted_edgelist /N/u2/t/taufique/Codes/gclust-jungle/data/email-Eu-core/email-Eu-core.edgelist /N/u2/t/taufique/Codes/gclust-jungle/data/email-Eu-core/email-Eu-core.bcsr
    weighted = None
    with open(input_file) as f:
        first_line = f.readline()
        tokens = first_line.split(" ")
        if len(tokens) > 2:
            weighted = True
        else:
            weighted = False

    cmdlist = ["python", "dependencies/verse/python/convert.py", "--format", "edgelist", input_file, output_file]
    if weighted == True:
        cmdlist = ["python", "dependencies/verse/python/convert.py", "--format", "weighted_edgelist", input_file, output_file]
    subprocess.run(cmdlist)
    print("Written:", output_file)
        
if __name__=="__main__":
    f = open('config.json',)
    config = json.load(f)
    dset = config["dataset"]
    # print(len(ds_config));
    for item in dset:
        if(item["convert"]):
            print("Converting", item["name"])
            for spec in item["convert"]:
                output_file = item["location"] + "/" + item["filename"] + "." + spec["to"]
                output_file_path = Path(output_file)
                if output_file_path.is_file():
                    # The output file is already there. No need to convert.
                    print(output_file, "already available")
                    pass
                else:
                    input_file = item["location"] + "/" + item["filename"] + "." + spec["from"]
                    input_file_path = Path(input_file)
                    if input_file_path.is_file():
                        # Do something
                        if (spec["from"] == "mtx" and spec["to"] == "edgelist"):
                            mtx_to_edgelist(input_file, output_file)
                        elif (spec["from"] == "mtx" and spec["to"] == "pajek"):
                            mtx_to_pajek(input_file, output_file)
                        elif (spec["from"] == "edgelist" and spec["to"] == "bcsr"):
                            edgelist_to_bcsr(input_file, output_file)
                        else:
                            print("I do not know how to convert", spec["from"], "to", spec["to"])
                    else:
                        print(input_file, "does not exist")
        else:
            print(item["name"], "no conversion")
