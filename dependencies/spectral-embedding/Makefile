IGRAPH_INCLUDE=../igraph/install/include/igraph
IGRAPH_LIB=../igraph/install/lib64

spectral-embedding: main.cpp
	g++ -fopenmp main.cpp \
		-I$(IGRAPH_INCLUDE) \
		-L$(IGRAPH_LIB) \
		-ligraph -lm\
		-o spectral-embedding

all: spectral-embedding

clean:
	rm -f spectral-embedding
