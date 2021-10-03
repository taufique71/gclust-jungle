IGRAPH_INCLUDE=../igraph/install/include/igraph
IGRAPH_LIB=../igraph/install/lib64

spectral-modularity: main.cpp
	g++ -fopenmp main.cpp \
		-I$(IGRAPH_INCLUDE) \
		-L$(IGRAPH_LIB) \
		-ligraph -lm\
		-o spectral-modularity

all: spectral-modularity

clean:
	rm -f spectral-modularity
