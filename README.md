# Auto Discover

[![Supported Versions](https://img.shields.io/pypi/pyversions/autodiscover.svg)](https://pypi.python.org/pypi/autodiscover)
[![PyPI version](https://badge.fury.io/py/autodiscover.svg)](https://pypi.python.org/pypi/autodiscover)
[![Maintainability](https://api.codeclimate.com/v1/badges/d9790fa518d3d54f37c5/maintainability)](https://codeclimate.com/github/nicolaszein/autodiscover/maintainability)
[![CircleCI](https://circleci.com/gh/nicolaszein/autodiscover/tree/master.svg?style=svg)](https://circleci.com/gh/nicolaszein/autodiscover/tree/master)

Auto Discover modules in python

Installing
----------

Install with **pip**:

```sh
$ pip install autodiscover
```


Usage
----------

```py
from pathlib import Path
from autodiscover import AutoDiscover

path = Path('path/to/module')
autodiscover = AutoDiscover(path)

autodiscover()
```

#### **With pattern**

```py
from pathlib import Path
from autodiscover import AutoDiscover

path = Path('path/to/module')
autodiscover = AutoDiscover(path, pattern="models.py")

autodiscover()
```
it will import all **models.py** from given path


Tests
----------
```sh
$ python -m unittest
```
