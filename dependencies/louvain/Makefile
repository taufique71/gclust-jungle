IGRAPH_INCLUDE=../igraph/install/include/igraph
IGRAPH_LIB=../igraph/install/lib64

louvain: main.cpp
	g++ -fopenmp main.cpp \
		-I$(IGRAPH_INCLUDE) \
		-L$(IGRAPH_LIB) \
		-ligraph -lm\
		-o louvain

all: louvain

clean:
	rm -f louvain
