# demo-pipeline

ENCODE DEMO pipeline
========================

This pipeline is designed for training purposes. The pipeline can be run on compute clusters with job submission engines or stand alone machines. It inherently makes uses of parallelized/distributed computing. Pipeline installation is also easy as most dependencies are automatically installed. The pipeline can be run end-to-end i.e. starting from raw FASTQ files all the way to trimmed FASTQ files. The pipeline supports single-end or paired-end data. The pipeline produces pretty HTML reports that include quality control measures specifically designed for Trimmomatic data, analysis of reproducibility.

# Installation / Tutorial

* [Google Cloud Platform](docs/tutorial_google.md)
* [DNANexus Platform with dxWDL CLI](docs/tutorial_dx_cli.md)
* [DNANexus Platform with Web UI](docs/tutorial_dx_web.md)
* [Stanford SCG](docs/tutorial_scg.md)
* [Stanford Sherlock 2.0](docs/tutorial_sherlock.md)
* [SLURM](docs/tutorial_slurm.md)
* [Sun GridEngine (SGE)](docs/tutorial_sge.md)
* [Local system with singularity](docs/tutorial_local_singularity.md)
* [Local system with docker](docs/tutorial_local_docker.md)
* [Local system with Conda](docs/tutorial_local_conda.md)

# [Input JSON](docs/input.md)

# [Output](docs/output.md)