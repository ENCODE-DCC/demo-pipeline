Tutorial for Stanford SCG cluster
==========================================

1. SSH to SCG's login node.
    ```
      $ ssh login.scg.stanford.edu
    ```

2. Git clone this pipeline and move into it.
    ```
      $ git clone https://github.com/ENCODE-DCC/demo-pipeline
      $ cd demo-pipeline
    ```

3. Download [cromwell](https://github.com/broadinstitute/cromwell).
    ```
      $ wget https://github.com/broadinstitute/cromwell/releases/download/35/cromwell-35.jar
      $ chmod +rx cromwell-35.jar
    ```

4. Set your account in `workflow_opts/scg.json`. If you don't have a SLURM account then remove the `slurm_account` from the JSON file. Ignore other runtime attributes for singularity.
    ```
      {
        "default_runtime_attributes" : {
          "slurm_account": "YOUR_SLURM_ACCOUNT"
        }
      }
    ```

5. Pull a singularity container for the pipeline. This will pull pipeline's docker container first and build a singularity one on `~/.singularity`.
    ```
      $ SINGULARITY_PULLFOLDER=~/.singularity singularity pull docker://quay.io/encode-dcc/demo-pipeline:template
    ```

6. Run a pipeline for the test sample.
    ```
      $ INPUT=examples/scg/input.json
      $ java -jar -Dconfig.file=backends/backend.conf -Dbackend.default=slurm_singularity cromwell-35.jar run toy.wdl -i ${INPUT} -o workflow_opts/scg.json
    ```

