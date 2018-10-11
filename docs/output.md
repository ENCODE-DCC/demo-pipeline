Output specification
====================

All output filenames keep some information from the corresponding input filenames. For example, if you start from `file1.fastq.gz` then the trimming task will output `trimmed.file1.fastq.gz`, and the plotting task will output `file1_untrimmed_file1_trimmed_quality_scores.png`.

1. `DNANexus`: If you choose to use `dxWDL` and run pipelines on DNANexus platform, then output will be stored on the specified output directory without any subdirectories.

2. `Cromwell`: Otherwise `Cromwell` will store outputs for each task under `cromwell-executions/[WORKFLOW_ID]/call-[TASK_NAME]/shard-[IDX]`.


|task|filename|description|
|-|-|-|
|trim|trimmed.*.fastq.gz|trimmed FASTQ|
|plot|*.quality_score.png|untrimmed versus trimmed FASTQ quality score plot|
