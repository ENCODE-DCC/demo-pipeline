Output specification
====================

All output filenames keep prefixes from corresponding input filenames. For example. If you have started from `file1.fastq.gz` - need to finish writing this section in a coherent manner.

1. `DNANexus`: If you choose to use `dxWDL` and run pipelines on DNANexus platform, then output will be stored on the specified output directory without any subdirectories.

2. `Cromwell`: Otherwise `Cromwell` will store outputs for each task under `cromwell-executions/[WORKFLOW_ID]/call-[TASK_NAME]/shard-[IDX]`.


|task|filename| description|
|-|-|-|
|trim| trimmed?_*.fastq.gz| Trimmed FASTQ|
|plot| *.trim_*.quality_score.png| Trimmed FASTQ quality scores plot |