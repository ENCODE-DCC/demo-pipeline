Tutorial for DNAnexus Platform (web)
====================================

All test data are shared on our public DNAnexus project. You don't have to download any data for testing our pipeline on DNAnexus platform.

There are two methods to run our pipeline on DNAnexus.

1) [Building your own DX workflow from `toy.wdl` with dxWDL (CLI)](tutorial_dx_cli.md)
2) Using a pre-built DX workflow on our public DX project (Web UI)

This document describes instruction for the item 2).

1. Sign up for a [DNAnexus account](https://platform.dnanexus.com/register).

2. Create a new [DX project](https://platform.dnanexus.com/projects) by clicking on "+New Project" on the top left.

3. Move to one of the following workflow directories according to the platform you have chosen for your project (AWS or Azure - AWS is slightly faster). These DX workflows are pre-built with all parameters defined.

* [AWS demo workflow](https://platform.dnanexus.com/projects/BKpvFg00VBPV975PgJ6Q03v6/data/Demo/workflows)
* [Azure demo workflow]()

4. Copy it to your project by right-clicking on the DX workflow `toy` and choose "Copy". 

5. Choose your project and create a folder for the test run by clicking on the "Folder+" icon.

6. Click on "Copy into this folder" on the bottom left.

7. Move to the target folder and click on the DX workflow `toy`.

9. Specify an output directory by clicking "Workflow Actions" on the top right. Click on "Set output folder" and choose an output folder.

10. Click on "Run as Analysis..." and you will be automatically redirected to the "Monitor" tab.

11. It will take about 15 minutes (30 minutes on Azure). You will be able to find all outputs in the output folder you specified.

11. See full specification for [input JSON file](input.md).
