Tutorial for general UNIX computers with docker
===============================================

1. Git clone this pipeline and move into it.
    ```
      $ git clone https://github.com/ENCODE-DCC/demo-pipeline
      $ cd demo-pipeline
    ```

2. Download [cromwell](https://github.com/broadinstitute/cromwell).
    ```
      $ wget https://github.com/broadinstitute/cromwell/releases/download/35/cromwell-35.jar
      $ chmod +rx cromwell-35.jar
    ```
    
3. Run a pipeline for the test sample.
    ```
      $ INPUT=examples/local/input.json
      $ java -jar -Dconfig.file=backends/backend.conf cromwell-35.jar run toy.wdl -i ${INPUT} -o workflow_opts/docker.json
    ```

4. It will take a few minutes. You will be able to find all outputs on `cromwell-executions/toy/[RANDOM_HASH_STRING]/`. See [output directory structure](output.md) for details.

5. See full specification for [input JSON file](input.md).