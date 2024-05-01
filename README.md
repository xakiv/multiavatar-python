# Multiavatar Fork

[Multiavatar](https://multiavatar.com) is a multicultural avatar generator, created by Gie Katon.

This repository is forked from the following [source](https://github.com/multiavatar/multiavatar-python)

## Installation

You may want to install this package in a python virtual environment: [More info](https://docs.python.org/3/library/venv.html)

```
pip install -e git+https://github.com/xakiv/multiavatar-python.git
```

## Usage

```
>>> from multiavatar.multiavatar import multiavatar
>>> avatar_svg = multiavatar("coucou", discard_env=False, style={}, sha256_randomizer=True)
>>> print(avatar_svg)
```

## More Information

The purpose of this fork is to play around with [Jinja2](https://palletsprojects.com/p/jinja/) templating,

hence the separation between logical process in python and SVG rendering through a Jinja template [avatar.svg](multiavatar/templates/avatar.svg).

The style configuration has been moved to [style.json](multiavatar/config/style.json).
