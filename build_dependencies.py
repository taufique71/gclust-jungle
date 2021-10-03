import os
from pathlib import Path
import subprocess

def build_infomap():
    print("[build_infomap]")
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/infomap")
    if Path("./Infomap").is_file():
        return
    cmdlist = ["make"]
    subp = subprocess.Popen(cmdlist)
    subp.wait()

def build_igraph():
    print("[build_igraph]")
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/igraph")
    if Path("install").is_dir():
        return
    os.mkdir("build")
    os.mkdir("install")
    os.chdir("build")
    
    cmdlist = [
                "cmake",
                "..",
                "-DCMAKE_INSTALL_PREFIX="+"../install",
                "-DIGRAPH_USE_INTERNAL_BLAS=ON",
                "-DIGRAPH_USE_INTERNAL_LAPACK=ON",
                "-DIGRAPH_USE_INTERNAL_ARPACK=ON",
                "-DIGRAPH_USE_INTERNAL_GLPK=ON",
                "-DIGRAPH_USE_INTERNAL_CXSPARSE=ON",
                "-DIGRAPH_USE_INTERNAL_GMP=OFF"
            ]
    subprocess.run(cmdlist)
    subprocess.run(["cmake", "--build", "."])
    subprocess.run(["cmake", "--install", "."])

def build_louvain():
    print("[build_louvain]")
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/louvain")
    if Path("./louvain").is_file():
        return
    cmdlist = ["make", "louvain"]
    subp = subprocess.Popen(cmdlist)
    subp.wait()

def build_spectral_modularity():
    print("[build_spectral_modularity]")
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/spectral-modularity")
    if Path("./spectral-modularity").is_file():
        return
    cmdlist = ["make", "all"]
    subp = subprocess.Popen(cmdlist)
    subp.wait()


if __name__=="__main__":
    build_infomap()
    build_igraph()
    build_louvain()
    build_spectral_modularity()
