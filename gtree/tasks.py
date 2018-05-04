import pyRserve
import numpy as np

conn = pyRserve.connect(host='localhost',port=6311)

def compute_pairwise_distance(conn,model='K80')
    conn.r.infile_path = 
    r_script = '''
        library('ape')
        compute_distance <- function(file,model)
        {
            alignment_data <- read.dna(file=file,format='fasta')
            index <- attr(alignment_data,"dimnames")[[1]]
            distance_data <- dist.dna(aligment_data,model=model,as.matrix=TRUE)
            result <- list(a=distance_data,b=index)
            return(result)
        }
        result <- compute_distance(infile_path,model)
        distance_data <- result$a
        index <- result$b
        '''
    con.eval(r_script)
    distance_data_ndarray = np.array(conn.r.distance_data)
    index = list(conn.r.index)
    return distance-data_ndarray,index

distance_data_ndarrat,index = compute_pairwise_distance(conn,model)
