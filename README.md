# Adinkras
Generating and storing permutation matrices for nebulous purposes

### Quickstart

#### Generator
Move `generator.py` into your working directory.

In your other files, you can then run this to get a list of working 8x16 matrices:

```
from generator import recover_working_eight_by_sixteens

...

list_of_8x16_matrices = recover_working_eight_by_sixteens()
```

This method stores the results on the first call, then retrieves them from file every future call.

If this doesn't work for whatever reason, you can also recompute them with 

```
from generator import get_working_8x16s

...

list_of_8x16_matrices = get_working_8x16s()
```

#### Negating column combinations
Move `generator.py` and `negate_column_combinations.py` into your working directory.

In your other files, you can run this to get a list of matrices with all combinations of columns negated:

```
from negate_column_combinations import generate_negated_column_combinations

...

numpy_matrices = (list of matrices to combine and negate columns from)
column_negated_matrices = generate_negated_column_combinations(numpy_matrices)
```

If you just want the column-combination negated versions of the working 8x16s from above, you can also just run `negate_column_combinations.py` in a directory with `generator.py` in it.
