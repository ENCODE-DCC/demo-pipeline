[![CircleCI](https://circleci.com/gh/ENCODE-DCC/demo-pipeline/tree/master.svg?style=svg)](https://circleci.com/gh/ENCODE-DCC/demo-pipeline/tree/master)

<p align="center">
<a href="https://www.encodeproject.org">
  <img style="float:left;" width="200" src="https://www.genome.gov/images/feature_images/encode_logo.gif">
</a>
</p>

ENCODE demo-pipeline
========================

This pipeline demonstrates the ENCODE pipeline reproducibility framework. Any pipeline deployed in this framework can be run on the cloud, on compute clusters with job-submission engines, or on stand-alone machines. It inherently makes use of parallelized/distributed computing. Pipeline installation is simple as most dependencies are automatically installed.

Here we implement a simple bioinformatics pipeline but surround it with all of the ENCODE pipeline reproducibility infrastructure.  The bioinformatic task is to use the [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic) software to trim input FASTQs. The output includes the trimmed FASTQ and a plot of FASTQ quality scores before and after trimming. For simplicity this demo supports only single-end FASTQs.

After experimenting with this repo you can create your own fork and use it as a template to deploy your own pipeline, inheriting all of the multi-platform and reproducibility features.


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

4. Examine output JSON:
```js
{
  "outputs": {
    "toy.trimmed_output": ["[cromwell/plot/task/execution/path]/trimmed.file1.fastq.gz"],
    "toy.plots": ["[cromwell/plot/task/execution/path]/file1_untrimmed_file1_trimmed_quality_scores.png"]
  },
  "id": "abc123"
}
```

5. Examine quality score plot:
```bash
# Mac only
$ open [cromwell/plot/task/execution/path]/file1_untrimmed_file1_trimmed_quality_scores.png 
```
<p align="center">
<img style="float:left;" width="1000" src="https://raw.githubusercontent.com/ENCODE-DCC/demo-pipeline/master/examples/local/output_plot/file1_untrimmed_file1_trimmed_quality_scores.png">
</p>


# Installation/tutorial

* [Local system with docker](docs/tutorial_local_docker.md)
* [Local system with singularity](docs/tutorial_local_singularity.md)
* [Google Cloud Platform](docs/tutorial_google.md)
* [DNANexus Platform with dxWDL CLI](docs/tutorial_dx_cli.md)
* [DNANexus Platform with Web UI](docs/tutorial_dx_web.md)
* [Stanford SCG](docs/tutorial_scg.md)
* [Stanford Sherlock 2.0](docs/tutorial_sherlock.md)


### [Input](docs/input.md)

### [Output](docs/output.md)
