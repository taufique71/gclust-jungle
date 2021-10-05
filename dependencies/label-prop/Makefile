IGRAPH_INCLUDE=../igraph/install/include/igraph
IGRAPH_LIB=../igraph/install/lib64

label-prop: main.cpp
	g++ -fopenmp main.cpp \
		-I$(IGRAPH_INCLUDE) \
		-L$(IGRAPH_LIB) \
		-ligraph -lm\
		-o label-prop 

all: label-prop

clean:
	rm -f label-prop
