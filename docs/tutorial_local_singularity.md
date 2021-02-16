# Running pipeline locally with Singularity

1. Install [singularity](https://www.sylabs.io/guides/2.6/user-guide/installation.html)

2. Get the code and move to the repo directory:

```bash
  $ git clone https://github.com/ENCODE-DCC/demo-pipeline
  $ cd demo-pipeline
```

3. Install [Caper](https://github.com/ENCODE-DCC/caper/):

```bash
  $ pip install caper
```

4. Run pipeline:

```bash
  $ caper run toy.wdl -i examples/local/input.json --singularity --no-build-singularity
```

5. See outputs in `cromwell-executions/toy/[RUNHASH]`.
