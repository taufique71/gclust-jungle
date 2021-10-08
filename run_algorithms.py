import os
from pathlib import Path
import networkx as nx
import scipy as sp
from scipy import io as spio
import json
import subprocess
import time
import sys

MAX_EXEC_TIME = 7200 # 3 hours

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

def run_louvain_parallel(config):
    print("[run_louvain_parallel]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/louvain-parallel")
    cmdlist = [
                "python",
                "./louvain-parallel.py",
                config["location"] + "/" + config["filename"] + "." + "edgelist",
                config["location"] + "/" + config["filename"] + "." + "louvain-parallel",
                "128"
            ]
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"louvain-parallel"+"."+"stats", "w") as f:
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

def run_mcl(config):
    print("[run_mcl]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/mcl-14-137/install/bin")
    cmdlist = [
                "./mcl",
                config["location"] + "/" + config["filename"] + "." + "edgelist",
                "--abc",
                "-o",
                config["location"] + "/" + config["filename"] + "." + "mcl"
            ]
    # print(" ".join(cmdlist))
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"mcl"+"."+"stats", "w") as f:
        content = str(subp.poll()) + " " + str(vm_size) + " " + str(exec_time) + "\n"
        f.write(content)
        f.close()


def run_verse(config):
    print("[run_verse]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/verse/src")
    cmdlist = [
                "./verse",
                "-input",
                config["location"] + "/" + config["filename"] + "." + "bcsr",
                "-output",
                config["location"] + "/" + config["filename"] + "." + "verse-emb",
                "-dim 128",
                "-alpha 0.85",
                "-threads 1",
                "-nsample 3"
            ]
    print(" ".join(cmdlist))
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"verse-emb"+"."+"stats", "w") as f:
        content = str(subp.poll()) + " " + str(vm_size) + " " + str(exec_time) + "\n"
        f.write(content)
        f.close()

def run_spectral_embedding(config):
    print("[run_spectral_embedding]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/spectral-embedding")
    cmdlist = [
                "./spectral-embedding",
                config["location"] + "/" + config["filename"] + "." + "edgelist",
                config["location"] + "/" + config["filename"] + "." + "spec-emb",
                "128"
            ]
    print(" ".join(cmdlist))
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"spec-emb"+"."+"stats", "w") as f:
        content = str(subp.poll()) + " " + str(vm_size) + " " + str(exec_time) + "\n"
        f.write(content)
        f.close()

def run_label_prop(config):
    print("[run_label_prop]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/label-prop")
    cmdlist = [
                "./label-prop",
                config["location"] + "/" + config["filename"] + "." + "edgelist",
                config["location"] + "/" + config["filename"] + "." + "label-prop"
            ]
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"label-prop"+"."+"stats", "w") as f:
        content = str(subp.poll()) + " " + str(vm_size) + " " + str(exec_time) + "\n"
        f.write(content)
        f.close()

def run_gn_edge_btn(config):
    print("[run_gn_edge_btn]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/gn-edge-btn")
    cmdlist = [
                "./gn-edge-btn",
                config["location"] + "/" + config["filename"] + "." + "edgelist",
                config["location"] + "/" + config["filename"] + "." + "gn-edge-btn"
            ]
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"gn-edge-btn"+"."+"stats", "w") as f:
        content = str(subp.poll()) + " " + str(vm_size) + " " + str(exec_time) + "\n"
        f.write(content)
        f.close()

def run_kernighan_lin(config):
    print("[run_kernighan_lin]:", config["name"])
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/kernighan-lin")
    cmdlist = [
                "python",
                "./kernighan-lin.py",
                config["location"] + "/" + config["filename"] + "." + "mtx",
                config["location"] + "/" + config["filename"] + "." + "kernighan-lin",
                "128"
            ]
    subp = subprocess.Popen(cmdlist)
    (vm_size, exec_time) = process_stat(subp)
    if exec_time > MAX_EXEC_TIME:
        subp.kill()
        subp.wait()
    with open(config["location"]+"/"+config["filename"]+"."+"kernighan-lin"+"."+"stats", "w") as f:
        content = str(subp.poll()) + " " + str(vm_size) + " " + str(exec_time) + "\n"
        f.write(content)
        f.close()
        
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
        for alg in algset:
            print("Running", alg, "on", item["name"])
            if alg == "infomap":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"infomap"+"."+"stats")
                if not stat_file_path.exists():
                    run_infomap(item)
            elif alg == "louvain":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"louvain"+"."+"stats")
                if not stat_file_path.exists():
                    run_louvain(item)
            elif alg == "louvain-parallel":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"louvain-parallel"+"."+"stats")
                if not stat_file_path.exists():
                    run_louvain_parallel(item)
            elif alg == "spectral-modularity":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"spectral-modularity"+"."+"stats")
                if not stat_file_path.exists():
                    run_spectral_modularity(item)
            elif alg == "mcl":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"mcl"+"."+"stats")
                if not stat_file_path.exists():
                    run_mcl(item)
            elif alg == "verse-emb":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"verse-emb"+"."+"stats")
                if not stat_file_path.exists():
                    run_verse(item)
            elif alg == "spec-emb":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"spec-emb"+"."+"stats")
                if not stat_file_path.exists():
                    run_spectral_embedding(item)
            elif alg == "label-prop":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"label-prop"+"."+"stats")
                if not stat_file_path.exists():
                    run_label_prop(item)
            elif alg == "gn-edge-btn":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"gn-edge-btn"+"."+"stats")
                if not stat_file_path.exists():
                    run_gn_edge_btn(item)
            elif alg == "kernighan-lin":
                stat_file_path = Path(item["location"]+"/"+item["filename"]+"."+"kernighan-lin"+"."+"stats")
                if not stat_file_path.exists():
                    run_kernighan_lin(item)

