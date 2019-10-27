# Auto Discover

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
