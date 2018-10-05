workflow toy {
    # inputs
    Array[File] fastqs
    Array[File] trimmed_fastqs = []
    Int MINLEN
    Int LEADING
    Int TRAILING
    String SLIDINGWINDOW

    Int number_of_fastqs = length(fastqs)
    Int number_of_trimmed_fastqs = length(trimmed_fastqs)

    scatter (i in range(number_of_fastqs-number_of_trimmed_fastqs)){
        call trim { input:
            fastq_file = fastqs[i],
            min_length = MINLEN,
            leading = LEADING,
            trailing = TRAILING,
            sliding_window = SLIDINGWINDOW
        }      
    }

    Array[File] trimmed_fastqs_ = flatten([trim.file, trimmed_fastqs])

    scatter (i in range(number_of_fastqs)){
        call plot { input:
            before_trimming = fastqs[i],
            after_trimming = trimmed_fastqs_[i]
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

task plot {
    File before_trimming
    File after_trimming

    command {
        touch plot.png
    }

    output {
        File plot = glob('plot.png')
    }
    
    runtime {
        docker: "quay.io/encode-dcc/demo-pipeline:v1"
    }
}