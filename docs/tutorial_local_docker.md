Tutorial for general UNIX computers with docker
===============================================

1. Git clone this pipeline and move into it.
    ```
      $ git clone https://github.com/ENCODE-DCC/demo-pipeline
      $ cd demo-pipeline
    ```

2. Install [Caper](https://github.com/ENCODE-DCC/caper/).
    ```
      $ pip install caper
    ```

3. Run a pipeline for the test sample.
    ```
      $ caper run toy.wdl -i examples/local/input.json --docker
    ```

4. It will take a few minutes. You will be able to find all outputs on `cromwell-executions/toy/[RANDOM_HASH_STRING]/`. See [output directory structure](output.md) for details.

5. See full specification for [input JSON file](input.md).
