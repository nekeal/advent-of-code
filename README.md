# Solutions for Advent of Code in Python

This project uses [aoc-python-cli](https://nekeal.github.io/advent-of-code-python-cli) for 
scaffolding the challenge for a given day, verifying the solution, and auto submitting it to the Advent of Code website.

---
## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.13+
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```
### Scaffold a new day
If you want get your puzzle input downloaded automatically, you need to set the `AOC_SESSION`
environment variable to your [session cookie](https://github.com/wimglenn/advent-of-code-wim/issues/1. Then run:

```sh
aoc new-day <day>
```

### Run solution for a given day

```sh
aoc run <day>
```

### Testing

```sh
aoc verify <day>
```

### Pre-commit

Pre-commit hooks run all the auto-formatting (`ruff format`), linters (e.g. `ruff` and `mypy`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
pre-commit run --all-files
```

---

This project was generated using the [cookiecutter-python-package](https://github.com/nekeal/cookiecutter-python-package) template.
