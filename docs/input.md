Input JSON
==========

An input JSON file includes all input parameters and metadata for running pipelines:

1) Input FASTQ file paths/URIs.
2) Pipeline parameters.
3) Resource for instances/jobs.

## For DNANexus CLI users

dxWDL (DNANexus CLI for WDL) does not support definition of task level variables with a prefix `toy.` in an input JSON file. Therefore, `toy.[TASK_NAME].[VAR_NAME]` should be replaced with `[TASK_NAME].[VAR_NAME]`. Simply remove a prefix `toy.` for task level variables. BUT DO NOT REMOVE it for workflow level variables. For example, `toy.qc_report.name` is a task (task `qc_report` in a workflow `toy`) level variable so it should be replaced with `qc_report.name`. But `toy.genome_tsv` is a workflow (`toy`) level variable, so you need to keep it the same. This is the only difference between DNANexus CLI and other platforms.

## Input data file

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


* `"toy.fastqs"` : 1-dimensional array with single end FASTQ file path/URI.
* `"toy.LEADING"` : .
* `"toy.TRAILING"` : .
* `"toy.MINLEN"` : .
* `"toy.SLIDINGWINDOW"` : .
* `"toy.bar_color"` : .
* `"toy.flier_color"` : .
* `"toy.plot_color"` : .

## Resource

**RESOURCES DEFINED IN AN INPUT JSON ARE PER TASK**. For example, if you have FASTQs for 2 replicates (2 tasks) and set `cpu` for `bowtie2` task as 4 then total number of cpu cores to map FASTQs is 2 x 4 = 8.

CPU (`cpu`), memory (`mem_mb`) settings are used for submitting jobs to cluster engines (SGE and SLURM) and Cloud platforms (Google Cloud Platform, AWS, ...). VM instance type on cloud platforms will be automatically chosen according to each task's `cpu` and `mem_mb`. Number of cores for tasks without `cpu` parameter is fixed at 1.

* `"toy.trim.cpu"` : (optional) Number of cores for `trim` (default: 2).
* `"toy.trim.mem_mb"` : (optional) Max. memory limit in MB for `trim` (default: 10000).

Disks (`disks`) is used for Cloud platforms (Google Cloud Platforms, AWS, ...).

* `"toy.trim.disks"` : (optional) Disks for `trim` (default: "local-disk 100 HDD").

Walltime (`time`) settings (for SGE and SLURM only).

* `"toy.trim.time_hr"` : (optional) Walltime for `trim` (default: 24).

