workflow toy {
    # inputs
    Array[File] fastqs
    Int MINLEN
    Int LEADING
    Int TRAILING
    String SLIDINGWINDOW

    #determine range of scatter
    Int sequencing_runs_length = length(fastqs)
    
    scatter (i in range(sequencing_runs_length)){
        call trim { input:
            fastq_file = fastqs[i]
            min_length = MINLEN
            leading = LEADING
            trailing = TRAILING
            sliding_window = SLIDINGWINDOW
        }      
    }

    output {
        Array[Array[File]] output = trim.files
    }
}

task trim {
    File fastq_file
    Int min_length
    Int leading
    Int trailing
    String sliding_window
    
    command {
        python3 $(which trim.py) \
            --fastqs ${fastqs}
    }

    output{
        Array[File] files = glob('*.fastq.gz')
    }

    runtime {
        docker: "quay.io/encode-dcc/demo-pipeline:v1"
    }
}