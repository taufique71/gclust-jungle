#!/bin/bash

DATA_DIR="data"

if [ ! -d "$DATA_DIR" ]; then
    mkdir "$DATA_DIR"
fi
pushd "$DATA_DIR"

if [ ! -d "ca-GrQc" ]; then
    if [ ! -f "ca-GrQc.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/SNAP/ca-GrQc.tar.gz
    fi
    tar -xvzf ca-GrQc.tar.gz
fi

if [ ! -d "ca-CondMat" ]; then
    if [ ! -f "ca-CondMat.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/SNAP/ca-CondMat.tar.gz
    fi
    tar -xvzf ca-CondMat.tar.gz
fi

if [ ! -d "com-DBLP" ]; then
    if [ ! -f "com-DBLP.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/SNAP/com-DBLP.tar.gz
    fi
    tar -xvzf com-DBLP.tar.gz
fi

if [ ! -d "email-Eu-core" ]; then
    if [ ! -f "email-Eu-core.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/SNAP/email-Eu-core.tar.gz
    fi
    tar -xvzf email-Eu-core.tar.gz
fi

if [ ! -d "email-Enron" ]; then
    if [ ! -f "email-Enron.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/SNAP/email-Enron.tar.gz
    fi
    tar -xvzf email-Enron.tar.gz
fi

if [ ! -d "email-EuAll" ]; then
    if [ ! -f "email-EuAll.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/SNAP/email-EuAll.tar.gz
    fi
    tar -xvzf email-EuAll.tar.gz
fi

if [ ! -d "wiki-Talk" ]; then
    if [ ! -f "wiki-Talk.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/SNAP/wiki-Talk.tar.gz
    fi
    tar -xvzf wiki-Talk.tar.gz
fi


if [ ! -d "nh2010" ]; then
    if [ ! -f "nh2010.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/DIMACS10/nh2010.tar.gz
    fi
    tar -xvzf nh2010.tar.gz
fi

if [ ! -d "in2010" ]; then
    if [ ! -f "in2010.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/DIMACS10/in2010.tar.gz
    fi
    tar -xvzf in2010.tar.gz
fi

if [ ! -d "belgium_osm" ]; then
    if [ ! -f "belgium_osm.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/DIMACS10/belgium_osm.tar.gz
    fi
    tar -xvzf belgium_osm.tar.gz
fi

if [ ! -d "asia_osm" ]; then
    if [ ! -f "asia_osm.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/DIMACS10/asia_osm.tar.gz
    fi
    tar -xvzf asia_osm.tar.gz
fi

if [ ! -d "europe_osm" ]; then
    if [ ! -f "europe_osm.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/DIMACS10/europe_osm.tar.gz
    fi
    tar -xvzf europe_osm.tar.gz
fi

if [ ! -d "cnr-2000" ]; then
    if [ ! -f "cnr-2000.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/LAW/cnr-2000.tar.gz
    fi
    tar -xvzf cnr-2000.tar.gz
fi

if [ ! -d "in-2004" ]; then
    if [ ! -f "in-2004.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/LAW/in-2004.tar.gz
    fi
    tar -xvzf in-2004.tar.gz
fi

if [ ! -d "uk-2002" ]; then
    if [ ! -f "uk-2002.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/LAW/uk-2002.tar.gz
    fi
    tar -xvzf uk-2002.tar.gz
    sed '1,48d' uk-2002/uk-2002.mtx > uk-2002/uk-2002.edgelist
fi

if [ ! -d "delaunay_n22" ]; then
    if [ ! -f "delaunay_n22.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/DIMACS10/delaunay_n22.tar.gz
    fi
    tar -xvzf delaunay_n22.tar.gz
    sed '1,131d' delaunay_n22/delaunay_n22.mtx > delaunay_n22/delaunay_n22.edgelist
fi

if [ ! -d "delaunay_n24" ]; then
    if [ ! -f "delaunay_n24.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/DIMACS10/delaunay_n24.tar.gz
    fi
    tar -xvzf delaunay_n24.tar.gz
    sed '1,131d' delaunay_n24/delaunay_n24.mtx > delaunay_n24/delaunay_n24.edgelist
fi

if [ ! -d "com-LiveJournal" ]; then
    if [ ! -f "com-LiveJournal.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/SNAP/com-LiveJournal.tar.gz
    fi
    tar -xvzf com-LiveJournal.tar.gz
fi

if [ ! -d "com-Orkut" ]; then
    if [ ! -f "com-Orkut.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/SNAP/com-Orkut.tar.gz
    fi
    tar -xvzf com-Orkut.tar.gz
    sed '1,88d' com-Orkut/com-Orkut.mtx > com-Orkut/com-Orkut.edgelist
fi

if [ ! -d "webbase-2001" ]; then
    if [ ! -f "webbase-2001.tar.gz" ]; then
        wget https://sparse.tamu.edu/MM/LAW/webbase-2001.tar.gz
    fi
    tar -xvzf webbase-2001.tar.gz
else
    pushd webbase-2001
    if [ ! -f "webbase-2001.edgelist" ]; then
        sed '1,54d' webbase-2001.mtx > webbase-2001.edgelist
    fi
    popd
fi

if [ ! -d "viruses" ]; then
    mkdir "viruses"
    pushd "viruses"
    if [ ! -f "vir_vs_vir_30_50length_propermm.mtx" ]; then
        wget https://portal.nersc.gov/project/m1982/HipMCL/viruses/vir_vs_vir_30_50length_propermm.mtx
    fi
    popd
fi

if [ ! -d "archea" ]; then
    mkdir "archea"
    if [ ! -f "Renamed_arch_vs_arch_30_50length.indexed.mtx.gz" ]; then
        wget https://portal.nersc.gov/project/m1982/HipMCL/archaea/Renamed_arch_vs_arch_30_50length.indexed.mtx.gz
        gunzip -d Renamed_arch_vs_arch_30_50length.indexed.mtx.gz
        mv Renamed_arch_vs_arch_30_50length.indexed.mtx archea/
    fi
    pushd archea
    if [ ! -f "Renamed_arch_vs_arch_30_50length.indexed.edgelist" ]; then
        sed '1,2d' Renamed_arch_vs_arch_30_50length.indexed.mtx > Renamed_arch_vs_arch_30_50length.indexed.edgelist
    fi
    popd
fi

if [ ! -d "isolates-subgraphs" ]; then
    mkdir "isolates-subgraphs"
    pushd "isolates-subgraphs"
    if [ ! -f "subgraph2_iso_vs_iso_30_70length_ALL.m100.oneindexed.mtx" ]; then
        wget https://portal.nersc.gov/project/m1982/HipMCL/subgraphs/subgraph2_iso_vs_iso_30_70length_ALL.m100.oneindexed.mtx
    fi
    if [ ! -f "subgraph2_iso_vs_iso_30_70length_ALL.m100.oneindexed.edgelist" ]; then
        sed '1,2d' subgraph2_iso_vs_iso_30_70length_ALL.m100.oneindexed.mtx > subgraph2_iso_vs_iso_30_70length_ALL.m100.oneindexed.edgelist
    fi
    popd
fi

popd
