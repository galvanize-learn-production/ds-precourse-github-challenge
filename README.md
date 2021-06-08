# Docker Testable Project Template

## Instructions

1. Copy all files present (including `.gitignore`) to the repo where your testable project will be hosted.
2. Populate `test_requirements.py` with any packages the unit test suite will require.
3. Write your specific unit tests in `test.py`.

### Dockerfile

The `Dockerfile` contains instructions for building the docker image. This shouldn't need modification for the most part.

### Unit test requirements

The text file `test_requirements.txt` contains Python package names separated by newlines. Any external packages required by `test.py` must go here. For example, a unit test suite which imports `matplotlib`, `numpy`, and `pandas` would look like this:

```
matplotlib
numpy
pandas
```

### Unit test suite

The Python file `test.py` contains all unit tests to be run on the student's submission.

## Docker test script

The shell script `test.sh` is what Learn runs after the Docker image is finished building. This can contain anything, but will most likely need only to run the command `python3 ./test.py`.
