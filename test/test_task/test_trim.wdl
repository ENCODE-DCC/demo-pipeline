import "../toy.wdl" as toy

workflow trim {
    File fastq
    Int MINLEN
    Int LEADING
    Int TRAILING
    String SLIDINGWINDOW
    
    call toy.trim as trim { input:
        fastq_file = fastq,
        min_length = MINLEN,
        leading = LEADING,
        trailing = TRAILING,
        sliding_window = SLIDINGWINDOW
    }

    output {
        File trimmed_fastq = trim.file
    }
}
