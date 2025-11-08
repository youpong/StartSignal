# StartSignal
A micro:bit project — a reaction time measurement app inspired by the F1 start signal, where five lights turn on in sequence before GO.

![sample screen](./screen.png)

## Create and activate virtual environment(vent)
```bash
# create virtual environment
$ python -m venv .venv
# activate for Windows
$ .venv/bin/activate 
# activate for macOS / Linux
$ source .venv/bin/activate
```

## To Upgrade pip [if necessary]
```bash
$ pip install --upgrade pip
```

## Installing development dependency packages
```bash
$ pip install -r requirements-dev.txt
```

## Linting source files
```bash
$ flake8 source_files...
```
