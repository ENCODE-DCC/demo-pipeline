import "../../toy.wdl" as toy

workflow concatenate {
    Array[File] input_fastqs
    
    call toy.concatenate as concatenate { input:
        trimmed_fastqs = input_fastqs
    }

    output {
        File concatenated_fastq = concatenate.concatenated_fastq
    }
}
