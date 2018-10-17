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

5. Download [cromwell](https://github.com/broadinstitute/cromwell).
    ```
      $ wget https://github.com/broadinstitute/cromwell/releases/download/35/cromwell-35.jar
      $ chmod +rx cromwell-35.jar
    ```

6. Run a pipeline for the test sample.
    ```
      $ PROJECT=encode-workshop
      $ BUCKET=gs://encode-workshop-outputs
      $ INPUT=examples/google/input.json
      $ java -jar -Dconfig.file=backends/backend.conf -Dbackend.default=google -Dbackend.providers.google.config.project=${PROJECT} -Dbackend.providers.google.config.root=${BUCKET} cromwell-35.jar run toy.wdl -i ${INPUT} -o workflow_opts/docker.json
    ```

7. See full specification for [input JSON file](input.md).