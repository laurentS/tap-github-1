# tap-github

`tap-github` is a Singer tap for GitHub.

Build with the [Singer SDK](https://gitlab.com/meltano/singer-sdk).

## Installation

- [ ] `Developer TODO:` Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

```bash
pipx install tap-github
```

## Configuration

### Accepted Config Options

- [ ] `Developer TODO:` Provide a list of config options accepted by the tap.

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-github --about
```

### Source Authentication and Authorization

- [ ] `Developer TODO:` If your tap requires special access on the source system, or any special authentication requirements, provide those here.

## Usage

You can easily run `tap-github` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-github --version
tap-github --help
tap-github --config CONFIG --discover > ./catalog.json
```

## Developer Resources

- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_github/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-github` CLI interface directly using `poetry run`:

```bash
poetry run tap-github --help
```

### Testing with [Meltano](meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-github
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-github --version
# OR run a test `elt` pipeline:
meltano elt tap-github target-jsonl
```

One-liner to recreate output directory, run elt, and write out state file:

```bash
# Update this when you want a fresh state file:
TESTJOB=testjob1

# Run everything in one line
mkdir -p .output && meltano elt tap-github target-jsonl --job_id $TESTJOB && meltano elt tap-github target-jsonl --job_id $TESTJOB --dump=state > .output/state.json
```

### Singer SDK Dev Guide

See the [dev guide](../../docs/dev_guide.md) for more instructions on how to use the Singer SDK to 
develop your own taps and targets.
