# Adinkras
Generating and storing permutation matrices for nebulous purposes

### Quickstart
To get a list of working 8x16 matrices, move `main.py` into your working directory and run:

```
from main import get_working_8x16s

...

list_of_8x16_matrices = get_working_8x16s()
```

Alternatively, run
`python3 main.py`
in the working directory, and then recover them with

```
from main import recover_working_eight_by_sixteens

...

list_of_8x16_matrices = recover_working_eight_by_sixteens()
```

This method stores the results on the first call, then retrieves them from file every future call.
