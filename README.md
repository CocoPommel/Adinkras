# Adinkras
Generating and storing permutation matrices for nebulous purposes

### Quickstart
Move `main.py` into your working directory.

In your other files, you can then run this to get a list of working 8x16 matrices:

```
from main import recover_working_eight_by_sixteens

...

list_of_8x16_matrices = recover_working_eight_by_sixteens()
```

This method stores the results on the first call, then retrieves them from file every future call.

If this doesn't work for whatever reason, you can also recompute them with 

```
from main import get_working_8x16s

...

list_of_8x16_matrices = get_working_8x16s()
```
