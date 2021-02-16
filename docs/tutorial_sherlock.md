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

3. Install [Caper](https://github.com/ENCODE-DCC/caper/).
    ```
      $ pip install caper
    ```

4. Add the following line to your BASH startup script (`~/.bashrc` or `~/.bash_profile`).
    ```
      module load system singularity java
    ```

5. Run a pipeline for the test sample.
    ```
      $ INPUT=examples/scg/input.json
      $ caper run toy.wdl -i ${INPUT} --singularity -b slurm --slurm-partition [SLURM_PARTITION]
    ```
