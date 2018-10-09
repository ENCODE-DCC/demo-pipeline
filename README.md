<p align="center">
<a href="https://www.encodeproject.org">
  <img style="float:left;" width="200" src="https://www.genome.gov/images/feature_images/encode_logo.gif">
</a>
</p>

ENCODE demo-pipeline
========================

This pipeline is designed to demonstrate the ENCODE pipeline development framework. The pipeline can be run on compute clusters with job-submission engines or stand-alone machines. It inherently makes use of parallelized/distributed computing. Pipeline installation is simple as most dependencies are automatically installed. The pipeline supports only single-end FASTQs to avoid unnecessary complexity. The pipeline uses [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic) software to trim input FASTQs. The output includes the trimmed FASTQ and a plot of FASTQ quality scores before and after trimming.

# Local quickstart

1. Clone this repo and install dependencies:
   * [Java 8](https://www.java.com/en/download/) or higher.
   * [Cromwell](https://github.com/broadinstitute/cromwell/releases/download/35/cromwell-35.jar)
   * [Docker CE](https://docs.docker.com/install/)

2. Add single-end FASTQ and Trimmomatic SLIDINGWINDOW parameter (filter reads that drop below average quality score of 30 in two-base window) to `input.json`:
```js
{
    "toy.fastqs": [
        "test/test_data/file1.fastq.gz"
    ],
    "toy.SLIDINGWINDOW": "2:30"
}
```

3. Run WDL workflow using `input.json`, Cromwell, and Docker backend:
```bash
$ java -jar -Dconfig.file=backends/backend.conf cromwell-35.jar run toy.wdl -i input.json -o workflow_opts/docker.json
```

4. Examine quality score plot:
```bash
# Mac only
$ open [cromwell/plot/task/execution/path]/file1_untrimmed_file1_trimmed_quality_scores.png 
```
<p align="center">
<img style="float:left;" width="1000" src="https://raw.githubusercontent.com/ENCODE-DCC/demo-pipeline/documentation/examples/local/output_plot/file1_untrimmed_file1_trimmed_quality_scores.png">
</p>


# Installation/tutorial

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
