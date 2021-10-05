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
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return

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
    subp = subprocess.Popen(cmdlist)
    subp.wait()
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return

    cmdlist = ["cmake", "--build", "."]
    subp = subprocess.Popen(cmdlist)
    subp.wait()
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return
    
    cmdlist = ["cmake", "--install", "."]
    subp = subprocess.Popen(cmdlist)
    subp.wait()
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return

def build_louvain():
    print("[build_louvain]")
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/louvain")
    if Path("./louvain").is_file():
        return

    cmdlist = ["make", "louvain"]
    subp = subprocess.Popen(cmdlist)
    subp.wait()
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return

def build_spectral_modularity():
    print("[build_spectral_modularity]")
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/spectral-modularity")
    if Path("./spectral-modularity").is_file():
        return

    cmdlist = ["make", "all"]
    subp = subprocess.Popen(cmdlist)
    subp.wait()
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return

def build_label_prop():
    print("[build_label_prop]")
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/label-prop")
    if Path("./label-prop").is_file():
        return

    cmdlist = ["make", "all"]
    subp = subprocess.Popen(cmdlist)
    subp.wait()
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return

def build_mcl():
    print("[build_mcl]")
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/mcl-14-137")
    if Path("./install").is_dir():
        return

    os.mkdir("install")
    cmdlist = ["./configure", "--prefix="+os.environ["GCLUST_JUNGLE_HOME"]+"/dependencies/mcl-14-137/install/"]
    subp = subprocess.Popen(cmdlist)
    subp.wait()
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return

    cmdlist = ["make", "install"]
    subp = subprocess.Popen(cmdlist)
    subp.wait()
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return

def build_verse():
    print("[build_verse]")
    os.chdir(os.environ["GCLUST_JUNGLE_HOME"])
    os.chdir("dependencies/verse/src")
    if Path("./verse").is_file():
        return

    cmdlist = ["make"]
    subp = subprocess.Popen(cmdlist)
    subp.wait()
    if subp.poll() != 0:
        print("COMMAND FAILED:", " ".join(cmdlist))
        return


if __name__=="__main__":
    build_infomap()
    build_igraph()
    build_louvain()
    build_spectral_modularity()
    build_mcl()
    build_verse()
    build_label_prop()
