# Experimental module for AST transformations

## Install

```bash
pip install git+https://github.com/nvbn/__transformers__
```

## Usage

Available transformations:

* `ellipsis_partial` &ndash; `map(lambda x: x + 1, ...)` to `lambda y: map(lambda x: x + 1, y)`;
* `matmul_pipe` &ndash; `"hello world" @ print` to `print("hello world")`.

Enable transformations in code:

```python
from __transformers__ import ellipsis_partial, matmul_pipe
  
range(10) @ map(lambda x: x ** 2, ...) @ list @ print 
```

Run code with transformations:

```bash
➜ python -m __transformers__ -m python_module   
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

➜ python -m __transformers__ python/module/path.py                 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Manually enable transformations from code:
 
```python
from __transformers__ import setup

setup()

import module_that_use_transformers
```

## Rationale

* [Idea](https://nvbn.github.io/2016/08/09/partial-piping/);
* [AST transformations](https://nvbn.github.io/2016/08/09/partial-piping-ast/);
* [AST transformations on import](https://nvbn.github.io/2016/08/17/ast-import/).

## License MIT
