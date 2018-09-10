Django common and useful routines
===============================
> Common Utilities, simple, just `cutils`

Common things that can be useful in any Django projects.

### Requirements

```bash
python --version == 3.4.*, 3.5.*, 3.6.*
```

### Installation

```bash
pip install git+https://github.com/mu-team/django-cutils.git
```

### Distribution

```bash
pip install setuptools

python3 setup.py sdist
```

### Contribution

```bash
pip install -r requires.txt
```

### Overview

```python
from django_cutils import models

# monitors for any changes in the internal state of the child model when save and update.
class ExampleModel(models.TimestampModel): ...

# replaces the standard removal mechanism with a soft one.
class ExampleModel(models.SoftDeletionModel): ...

# Compilation of `TimestampModel` and `SoftDeletionModel`.
class ExampleModel(models.CUDModel): ...
```
