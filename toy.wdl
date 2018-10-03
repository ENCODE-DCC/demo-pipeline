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
            fastq_file = fastqs[i],
            min_length = MINLEN,
            leading = LEADING,
            trailing = TRAILING,
            sliding_window = SLIDINGWINDOW
        }      
    }

    output {
        Array[File] output = trim.file
    }
}

task trim {
    File fastq_file
    Int min_length
    Int leading
    Int trailing
    String sliding_window
    
    command {
        input_file=$(echo ${fastq_file} | sed 's/.*\///')
        java -jar /software/Trimmomatic-0.38/trimmomatic-0.38.jar SE -phred33 ${fastq_file} trimmed.$input_file LEADING:${leading} TRAILING:${trailing} SLIDINGWINDOW:${sliding_window} MINLEN:${min_length}
    }

    output{
        File file = glob('trimmed.*.fastq.gz')[0]
    }

    runtime {
        docker: "quay.io/encode-dcc/demo-pipeline:v1"
    }
}