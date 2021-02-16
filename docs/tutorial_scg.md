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

3. Install [Caper](https://github.com/ENCODE-DCC/caper/).
    ```
      $ pip install caper
    ```

4. Run a pipeline for the test sample. If you don't have a SLURM account then remove the `--slurm-account` argument.
    ```
      $ INPUT=examples/scg/input.json
      $ caper run -i toy.wdl ${INPUT} --singularity -b slurm --slurm-account [SLURM_ACCOUNT]
    ```
