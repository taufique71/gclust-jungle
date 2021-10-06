IGRAPH_INCLUDE=../igraph/install/include/igraph
IGRAPH_LIB=../igraph/install/lib64

gn-edge-btn: main.cpp
	g++ -fopenmp main.cpp \
		-I$(IGRAPH_INCLUDE) \
		-L$(IGRAPH_LIB) \
		-ligraph -lm\
		-o gn-edge-btn

all: gn-edge-btn

clean:
	rm -f gn-edge-btn
