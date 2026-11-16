**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requirements: Python 3.13 or newer and Git. Runtime dependencies: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly` and `scikit-learn`. Nothing else is needed to run the analysis.

## Windows (PowerShell)

Create and use a local `.venv`:

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model.git
cd 081-multivariable-regression-and-valuation-model
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, run `Set-ExecutionPolicy -Scope Process RemoteSigned` first; it only applies to the current window.

## Linux and macOS (bash)

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/081-multivariable-regression-and-valuation-model.git
cd 081-multivariable-regression-and-valuation-model
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run, test and open the notebook

The commands are the same on every system once the `.venv` is active. The third command draws the pictures of the steps into `docs/images`:

```bash
python -m pytest
python -m ruff check src tests
python -m boston_valuation.presentation.screenshots
python -m pip install -e ".[notebook]"
jupyter lab notebooks
```

`jupyter lab` needs the `notebook` extra (JupyterLab and the kernel). Open `notebooks/boston_valuation.ipynb` to run the steps, or the course's own notebooks next to it.

## Check the code with opengrep

Run opengrep before every push. On Windows the program is `~\.opengrep\cli\latest\opengrep.exe`; on Linux it is `~/.opengrep/cli/latest/opengrep`:

```bash
~/.opengrep/cli/latest/opengrep scan --config p/python src tests
```

Fix every finding before you push.

## Build the Doxygen documentation (optional)

```bash
doxygen Doxyfile
```

The pages are written to `docs/doxygen/html`.

**What you gain:** a repeatable set-up (one virtual environment per project), a package installed in editable mode, tests that prove each answer, and a static check before you share your code.
