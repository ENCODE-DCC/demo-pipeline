workflow toy {
    # inputs
    Array[File] fastqs = []
    Array[File] trimmed_fastqs = []
    Int MINLEN = 0
    Int LEADING = 0
    Int TRAILING = 0
    String SLIDINGWINDOW = "1:0"
    String bar_color = 'white'
    String flier_color = 'grey'
    String plot_color = 'darkgrid'

    Int number_of_fastqs = length(fastqs)
    Int number_of_trimmed_fastqs = length(trimmed_fastqs)

    scatter (i in range(number_of_fastqs - number_of_trimmed_fastqs)){
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
            after_trimming = trimmed_fastqs_[i],
            bar_color = bar_color,
            flier_color = flier_color,
            plot_color = plot_color
        }      
    }

    output {
        Array[File] trimmed_output = trim.file
        Array[File] plots = plot.plot_output
    }
}

task trim {
    File fastq_file
    Int min_length
    Int leading
    Int trailing
    String sliding_window
    
    command {
        input_file=$(basename ${fastq_file})
        java -jar /software/Trimmomatic-0.38/trimmomatic-0.38.jar \
        SE -phred33 ${fastq_file} trimmed.$input_file \
        LEADING:${leading} \
        TRAILING:${trailing} \
        SLIDINGWINDOW:${sliding_window} \
        MINLEN:${min_length}
    }

    output{
        File file = glob('trimmed.*.fastq.gz')[0]
    }
}

task plot {
    File before_trimming
    File after_trimming
    String bar_color
    String flier_color
    String plot_color
    Int? plot_width
    Int? plot_height

    command {
        python3 /software/demo-pipeline/src/plot_fastq_scores.py \
        --untrimmed ${before_trimming} \
        --trimmed ${after_trimming} \
        --bar-color ${bar_color} \
        --flier-color ${flier_color} \
        --plot-color ${plot_color} \
        ${'--plot-width ' + plot_width} \
        ${'--plot-height ' +  plot_height}
    }

    output {
        File plot_output = glob('*quality_scores.png')[0]
    }
}
