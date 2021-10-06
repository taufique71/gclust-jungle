/*
 *  Graph clustering with modularity optimization by leading eigenvectors
 * */

#include <igraph.h>
#include <math.h>
#include <omp.h>
#include <string>

int main(int argc, char *argv[]) {
    igraph_t graph;

    std::string infile(argv[1]);
    std::string outfile(argv[2]);
    FILE *fin;
    FILE *fout;
    fin = fopen(infile.c_str(), "r");
    fout = fopen(outfile.c_str(), "w");

    double t0, t1;
    
    fprintf(fout, "File: %s\n", infile.c_str());

    t0 = omp_get_wtime();
    igraph_read_graph_ncol(&graph, fin, NULL, IGRAPH_DIRECTED, IGRAPH_ADD_WEIGHTS_IF_PRESENT, IGRAPH_UNDIRECTED);
    t1 = omp_get_wtime();
    fprintf(fout, "Read: %lf seconds\n", t1-t0);
    fclose(fout);
    fout = fopen(outfile.c_str(), "a");

    long int n_edges = (long int ) ( igraph_ecount(&graph) );
    long int n_vertices = (long int) ( igraph_vcount(&graph) );
    fprintf(fout, "Vertices: %ld\n", n_vertices);
    fprintf(fout, "Edges: %ld\n", n_edges);
    
    igraph_integer_t ndim = 128;
    if(argc > 3){
        ndim = atoi(argv[3]);
    }
    igraph_matrix_t X;
    igraph_matrix_init(&X, n_vertices, ndim);
    igraph_vector_t eigvals;
    igraph_vector_init(&eigvals, 0);
    igraph_vector_init_seq(&eigvals, 0, ndim-1); // Singleton clusters

    // https://igraph.org/c/html/0.9.4/igraph-Arpack.html#igraph_arpack_options_t
    igraph_arpack_options_t options;
    igraph_arpack_options_init(&options);
    //// Default max iteration is 3000 in igraph. Increasing it to 5000.
    //options.mxiter = 5000; 

    t0 = omp_get_wtime();
    igraph_real_t modularity;
    igraph_integer_t nb_cluster;
    //igraph_community_leading_eigenvector(
            //&graph, // graph
            //NULL, // edge weights
            //NULL, // merges
            //&membership, // membership vector
            //n_vertices, // steps
            //&options, // options
            //&modularity, // modularity
            //0, // start
            //NULL, // eigenvalues
            //NULL, //eigenvectors
            //NULL, // history
            //NULL, // callback
            //NULL // extra callback parameter
            //);
    igraph_laplacian_spectral_embedding(
            &graph, // graph
            ndim, // The number of eigenvectors used for embedding
            NULL,
            IGRAPH_EIGEN_LM,
            IGRAPH_EMBEDDING_DAD,
            1,
            &X,
            NULL,
            &eigvals,
            &options
            );
    t1 = omp_get_wtime();
    fprintf(fout, "Compute: %lf seconds\n", t1-t0);

    for (int i = 0; i < igraph_matrix_nrow(&X); i++) {
        for (int j = 0; j < igraph_matrix_ncol(&X); j++) {
            fprintf(fout, "%lf ", (double)MATRIX(X, i, j));
        }
        fprintf(fout, "\n");
    }
    fprintf(fout, "\n");

    fclose(fin);
    fclose(fout);
    
    /* Free memory */
    igraph_vector_destroy(&eigvals);
    igraph_matrix_destroy(&X);
    igraph_destroy(&graph);

    return 0;
}
