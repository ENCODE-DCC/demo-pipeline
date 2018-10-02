workflow toy {
    # inputs
    Array[Array[File]] fastqs
    Int min_length

    #determine range of scatter
    Int sequencing_runs_length = length(fastqs)
    
    scatter (i in range(sequencing_runs_length)){
        call trim { input:
            fastqs = fastqs[i],
            min_length = min_length
        }      
    }

    output {
        Array[Array[File]] output = trim.files
    }
}

task trim {
    Array[File] fastqs
    Int min_length
    
    command {
        python3 $(which trim.py) \
            --fastqs ${fastqs}
    }

    output{
        Array[File] files = glob('*.fastq.gz')
    }

    runtime {
        docker: "quay.io/gabdank/toy:v3"
    }
}