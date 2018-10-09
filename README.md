<p align="center">
<a href="https://www.encodeproject.org">
  <img style="float:left;" width="200" src="https://www.genome.gov/images/feature_images/encode_logo.gif">
</p>

ENCODE demo-pipeline
========================

This pipeline is designed to demonstrate the ENCODE pipeline development framework. The pipeline can be run on compute clusters with job submission engines or stand-alone machines. It inherently makes use of parallelized/distributed computing. Pipeline installation is simple as most dependencies are automatically installed. The pipeline supports only single-end FASTQs to avoid unnecessary complexity. The pipeline uses Trimmomatic software to trim input FASTQs. The output includes the trimmed FASTQ and a plot of FASTQ quality scores before and after trimming.

# Installation / Tutorial

* [Local system with docker](docs/tutorial_local_docker.md)
* [Google Cloud Platform](docs/tutorial_google.md)
* [DNANexus Platform with dxWDL CLI](docs/tutorial_dx_cli.md)
* [DNANexus Platform with Web UI](docs/tutorial_dx_web.md)
* [Stanford SCG](docs/tutorial_scg.md)
* [Stanford Sherlock 2.0](docs/tutorial_sherlock.md)
* [SLURM](docs/tutorial_slurm.md)
* [Sun GridEngine (SGE)](docs/tutorial_sge.md)
* [Local system with singularity](docs/tutorial_local_singularity.md)


### [Input](docs/input.md)

### [Output](docs/output.md)

### [Testing](docs/testing.md)
