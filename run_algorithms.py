import os
from pathlib import Path
import networkx as nx
import scipy as sp
from scipy import io as spio
import json
import subprocess
import time

MAX_EXEC_TIME = 3600 # 1 hour

def process_stat(proc):
    peak_vm_size = 0
    proc_exec_time = 0
    tokens = []
    t0 = time.time()
    while (proc.poll() is None):
        filename = "/proc/" + str(proc.pid) + "/stat"
        with open(filename, "r") as f:
            text = f.read()
            tokens = text.split(" ")
            # https://man7.org/linux/man-pages/man5/proc.5.html
            peak_vm_size = max(peak_vm_size, int(tokens[22]))
            proc_exec_time = int(tokens[13]) + int(tokens[14])
        t1 = time.time()
        if(t1-t0 > MAX_EXEC_TIME):
            break
    t1 = time.time()
    return (peak_vm_size, t1-t0)

def run_infomap(config):
    # ./Infomap /N/u2/t/taufique/Codes/graph-clustering/data/ca-CondMat/ca-CondMat.triples ./outdir/ --two-level --flow-model undirected -N 1 -v --clu
    print("[run_infomap]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/infomap")
    cmdlist = [
                "./Infomap",
                config["location"] + "/" + config["filename"] + "." + "edgelist",
                config["location"],
                "--output", "clu",
                "--flow-model", "undirected",
                "-N", "1",
            ]
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"infomap"+"."+"stats", "w") as f:
        content = str(subp.poll()) + " " + str(vm_size) + " " + str(exec_time) + "\n"
        f.write(content)
        f.close()

def run_louvain(config):
    print("[run_louvain]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/louvain")
    cmdlist = [
                "./louvain",
                config["location"] + "/" + config["filename"] + "." + "edgelist",
                config["location"] + "/" + config["filename"] + "." + "louvain"
            ]
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"louvain"+"."+"stats", "w") as f:
        content = str(subp.poll()) + " " + str(vm_size) + " " + str(exec_time) + "\n"
        f.write(content)
        f.close()

def run_spectral_modularity(config):
    print("[run_spectral_modularity]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/spectral-modularity")
    cmdlist = [
                "./spectral-modularity",
                config["location"] + "/" + config["filename"] + "." + "edgelist",
                config["location"] + "/" + config["filename"] + "." + "spectral-modularity"
            ]
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"spectral-modularity"+"."+"stats", "w") as f:
        content = str(subp.poll()) + " " + str(vm_size) + " " + str(exec_time) + "\n"
        f.write(content)
        f.close()

        
if __name__=="__main__":
    f = open('config.json',)
    config = json.load(f)
    dset = config["dataset"]
    # print(len(ds_config));
    for item in dset:
        for alg in config["algorithms"]:
            print("Running", alg["name"], "on", item["name"])
            if alg["name"] == "infomap":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"infomap"+"."+"stats")
                print(stat_file_path.is_file())
                if not stat_file_path.exists():
                    run_infomap(item)
            elif alg["name"] == "louvain":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"louvain"+"."+"stats")
                if not stat_file_path.exists():
                    run_louvain(item)
            elif alg["name"] == "spectral-modularity":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"spectral-modularity"+"."+"stats")
                if not stat_file_path.exists():
                    run_spectral_modularity(item)

