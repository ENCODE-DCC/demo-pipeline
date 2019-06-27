Tutorial for Google Cloud Platform
===================================================

All test samples and data are shared on our public Google Cloud buckets. You don't have to download any data for testing our pipeline on Google Cloud.

1. Install [Google Cloud Platform SDK](https://cloud.google.com/sdk/downloads) and authenticate through it. You will be asked to enter verification keys. Get keys from the URLs they provide.
    ```
      $ gcloud auth login --no-launch-browser
      $ gcloud auth application-default login --no-launch-browser
    ```

2. If you see permission errors at runtime, then unset environment variable `GOOGLE_APPLICATION_CREDENTIALS` or add it to your BASH startup scripts (`$HOME/.bashrc` or `$HOME/.bash_profile`).
    ```
      unset GOOGLE_APPLICATION_CREDENTIALS
    ```

3. Set your default Google Cloud Project. Pipeline will provision instances on this project.
    ```
      $ gcloud config set project [YOUR_PROJECT_NAME]
    ```

4. Git clone this pipeline and move into it.
    ```
      $ git clone https://github.com/ENCODE-DCC/demo-pipeline
      $ cd demo-pipeline
    ```

5. Install [Caper](https://github.com/ENCODE-DCC/caper/) and [Croo](https://github.com/ENCODE-DCC/croo/).
    ```
      $ pip install caper
      $ pip install croo
    ```

6. Run a pipeline for the test sample.
    ```
      $ PROJECT=encode-workshop
      $ BUCKET=gs://encode-workshop-outputs
      $ INPUT=examples/google/input.json
      $ caper run toy.wdl -i ${INPUT} --use-docker -b gcp --gcp-prj ${PROJECT} --out-gcs-bucket ${BUCKET} --tmp-gcs-bucket ${BUCKET}
    ```

7. It will take a few minutes. After it finishes, use `croo` to copy and organize the pipeline outputs. You can then examine the pipeline outputs in this folder `output` on your local machine.
    ```
      $ croo gs://${BUCKET}/toy/[WF_ID]/metadata.json --out-dir output
    ```

8. See full specification for [input JSON file](input.md).
