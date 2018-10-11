Tutorial for DNAnexus Platform (CLI)
====================================

All test samples and genome data are shared on our public DNAnexus project. You don't have to download any data for testing our pipeline on DNAnexus platform.

There are two methods to run our pipeline on DNAnexus.

1) Building your own DX workflow from `atac.wdl` with dxWDL (CLI)
2) [Using a pre-built DX workflow on our public DX project (Web UI)](tutorial_dx_web.md)

This document describes instruction for the item 1).

1. Sign up for a [DNAnexus account](https://platform.dnanexus.com/register).

2. Create a new [DX project](https://platform.dnanexus.com/projects) with name `[YOUR_PROJECT_NAME]` by clicking on "+New Project" on the top left.

3. Git clone this pipeline.
    ```
      $ git clone https://github.com/ENCODE-DCC/demo-pipeline
    ```

4. Move to pipeline's directory.
    ```
      $ cd demo-pipeline
    ```

5. Download dxWDL.
    ```
      $ wget https://github.com/dnanexus/dxWDL/releases/download/0.78/dxWDL-0.78.jar
      $ chmod +rx dxWDL-0.78.jar
    ```

6. Choose an appropriate input for your project (AWS or Azure):
    * AWS (recommended as it is faster)
      ```
        $ INPUT=examples/dx/input.json
      ```
    * Azure
      ```
        $ INPUT=examples/dx_azure/input.json
      ```

7. Compile `toy.wdl` with the input JSON.
    ```
      $ PROJECT=[YOUR_PROJECT_NAME]
      $ OUT_FOLDER=/demo_pipeline_toy

      $ java -jar dxWDL-0.78.jar compile toy.wdl -project ${PROJECT} -f -folder ${OUT_FOLDER} -defaults ${INPUT} -extras workflow_opts/docker.json
    ```

8. Go to DNANexus [project page](https://platform.dnanexus.com/projects) and click on your project.

9. Move to the directory `/demo_pipeline_toy`.

10. You will find a DX workflow `toy` with all parameters pre-defined. Click on it. 

11. Specify an output directory by clicking "Workflow Actions" on the top right. Click on "Set output folder" and choose an output folder.

12. Click on "Run as Analysis..." and you will be automatically redirected to the "Monitor" tab.

13. It will take about 15 minutes to run (30 minutes on Azure). You will be able to find all outputs on your output folder.

14. See full specification for [input JSON file](input.md).
