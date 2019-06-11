# Running pipeline locally with Singularity

1. Install [singularity](https://www.sylabs.io/guides/2.6/user-guide/installation.html)

2. Build the singularity image for the pipeline. The following pulls the pipeline docker image, and uses that to construct the singularity image. The image will be stored in `~/.singularity`.
```
$ SINGULARITY_CACHEDIR=~/.singularity SINGULARITY_PULLFOLDER=~/.singularity singularity pull docker://quay.io/encode-dcc/demo-pipeline:template
```

3. Get the code and move to the repo directory:

```bash
  $ git clone https://github.com/ENCODE-DCC/demo-pipeline
  $ cd demo-pipeline
```

4. Run pipeline:

```bash
  $ java -jar -Dconfig.file=backends/backend.conf -Dbackend.default=singularity cromwell-35.jar run toy.wdl -i examples/local/input.json -o workflow_opts/singularity.json
```

5. See outputs in `cromwell-executions/toy/[RUNHASH]`.
