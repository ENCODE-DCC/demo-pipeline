Input JSON
==========

An input JSON file includes all input parameters and metadata for running pipelines:

1) Input FASTQ file paths/URIs.
2) Pipeline parameters.
3) Resource for instances/jobs.

## Example input JSON

    "toy.fastqs": [
        "test/test_data/file1.fastq.gz",
        "test/test_data/file2.fastq.gz"
    ],
    "toy.LEADING": 3,
    "toy.TRAILING": 3,
    "toy.MINLEN": 50,
    "toy.SLIDINGWINDOW": "3:5",
    "toy.bar_color": "white",
    "toy.flier_color": "grey",
    "toy.plot_color": "darkgrid"

## For DNANexus CLI users

dxWDL (DNANexus CLI for WDL) does not support definition of task level variables with a prefix `toy.` in an input JSON file. Therefore, `toy.[TASK_NAME].[VAR_NAME]` should be replaced with `[TASK_NAME].[VAR_NAME]`. Simply remove a prefix `toy.` for task level variables. BUT DO NOT REMOVE it for workflow level variables. This is the only difference between DNANexus CLI and other platforms.

## Input data file

|task|parameter|type|need|default|description|
|-|-|-|-|-|-|
|trim|toy.fastqs|array|required|[]|1-dimensional array with single-end FASTQ file path/URI|
|trim|toy.trimmed_fastqs|array|optional|[]|1-dimensional array with single-end trimmed FASTQ file path/URI (note order of trimmed_fastqs must match order of raw fastqs)|

## Pipeline parameters

|task|parameter|type|need|default|description|
|-|-|-|-|-|-|
|trim|toy.LEADING|int|optional|0|minimum quality required to keep a base from start of read|
|trim|toy.TRAILING|int|optional|0|minimum quality required to keep a base from end of read|
|trim|toy.MINLEN|int|optional|0|minimum length of reads to keep|
|trim|toy.SLIDINGWINDOW|string|optional|"1:0"|number of bases to average across:average quality required|
|plot|toy.bar_color|string|optional|"white"|color of box plot bars|
|plot|toy.flier_color|string|optional|"grey"|color of outlier points|
|plot|toy.plot_color|string|optional|"darkgrid"|color/style of plot background, must be one of ['whitegrid', 'darkgrid', 'white', 'ticks']|


## Resource

**RESOURCES DEFINED IN AN INPUT JSON ARE PER TASK**. For example, if you have two input FASTQs (two tasks) and set `cpu` for `trimming` task as four then total number of cpu cores to trim FASTQs is 2 x 4 = 8.

CPU (`cpu`), memory (`mem_mb`) settings are used for submitting jobs to cluster engines (SGE and SLURM) and Cloud platforms (Google Cloud Platform, AWS, ...). VM instance type on cloud platforms will be automatically chosen according to each task's `cpu` and `mem_mb`. Number of cores for tasks without `cpu` parameter is fixed at 1.

|task|parameter|type|need|default|description|
|-|-|-|-|-|-|
|trim|toy.trim.cpu|int|optional|2|number of cores for task|
|trim|toy.trim.mem_mb|int|optional|10000|maximum memory limit in MB for task|
|trim|toy.trim.disks|string|optional|"local-disk 100 HDD"|disks for task, only used for used for Cloud platforms (Google Cloud Platforms, AWS, etc.)|
|trim|toy.trim.time_hr|int|optional|24|walltime for task, for SGE and SLURM only|
