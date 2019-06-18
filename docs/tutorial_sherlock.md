Tutorial for Stanford Sherlock 2.0 cluster
==========================================

1. SSH to Sherlock's login node.
    ```
      $ ssh login.sherlock.stanford.edu
    ```

2. Git clone this pipeline and move into it.
    ```
      $ git clone https://github.com/ENCODE-DCC/demo-pipeline
      $ cd demo-pipeline
    ```

3. Download [cromwell](https://github.com/broadinstitute/cromwell).
    ```
      $ wget https://github.com/broadinstitute/cromwell/releases/download/42/cromwell-42.jar
      $ chmod +rx cromwell-42.jar
    ```

4. Set your partition in `workflow_opts/sherlock.json`. If you don't have a partition then remove the `slurm_partition` object from the JSON file. Ignore other runtime attributes for singularity.
    ```
      {
        "default_runtime_attributes" : {
          "slurm_partition": "YOUR_SLURM_PARTITON"
        }
      }
    ```

5. Add the following line to your BASH startup script (`~/.bashrc` or `~/.bash_profile`).
    ```
      module load system singularity java
    ```

6. Pull a singularity container for the pipeline. This will pull pipeline's docker container first and build a singularity one on `~/.singularity`. Stanford Sherlock does not allow building a container on login nodes. Wait until you get a command prompt after `sdev`.
    ```
      $ sdev    # sherlock cluster does not allow building a container on login node
      $ SINGULARITY_CACHEDIR=~/.singularity SINGULARITY_PULLFOLDER=~/.singularity singularity pull docker://quay.io/encode-dcc/demo-pipeline:template
      $ exit    # exit from an interactive node
    ```

7. Run a pipeline for the test sample.
    ```
      $ INPUT=examples/sherlock/input.json
      $ java -jar -Dconfig.file=backends/backend.conf -Dbackend.default=slurm_singularity cromwell-42.jar run toy.wdl -i ${INPUT} -o workflow_opts/sherlock.json
    ```

