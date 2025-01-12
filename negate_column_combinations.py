from copy import deepcopy
from generator import recover_working_eight_by_sixteens
import itertools as it
import numpy as np
import pickle

INNER_COLUMNS_TO_NEGATE = [0, 1, 2, 3, -1, -1, -1, -1]



def combinations_of_negated_columns_of_matrix(matrix):
    combinations = []
    
    combinations_already_negated = [] # since every combination with -1s will occur more than once, keep track of the ones weve done already
    for set_of_columns_to_negate in it.combinations(INNER_COLUMNS_TO_NEGATE, 4):
        actual_set_of_columns_to_negate = [i for i in set_of_columns_to_negate if i != -1]
        if actual_set_of_columns_to_negate in combinations_already_negated:
            continue
        
        deep_matrix_copy = np.array(deepcopy(matrix)) # so we dont overwrite columns in the original template matrix
        for inner_column_to_negate in [i for i in set_of_columns_to_negate if i != -1]:
            for i in range(4):
                big_matrix_column_to_negate = 4*i + inner_column_to_negate # negate the inner column in the [i]th matrix column
                deep_matrix_copy[:,big_matrix_column_to_negate] *= -1 # multiply all entries in the [column_to_negate]th column by -1
            
        combinations.append(deep_matrix_copy)
        combinations_already_negated.append(actual_set_of_columns_to_negate)
            
    return combinations


def numpy_matrix_pretty(numpy_matrix):
    ret = ""
    for row in numpy_matrix:
        ret += "|  "
        for element in np.nditer(row):
            if element >= 0:
                ret += " {}  ".format(int(element + 0)) # element + 0 coerces negative zero to zero
            else:                                  # otherwise it looks like ass
                ret += "{}  ".format(int(element + 0))
        ret += "|\n"

    return ret


def generate_negated_column_combinations(matrices_to_negate_column_combinations_from):
    matrices_with_all_column_combinations_negated = []
    
    for matrix in matrices_to_negate_column_combinations_from:
        matrices_with_all_column_combinations_negated += combinations_of_negated_columns_of_matrix(matrix) # merge lists instead of making a list of lists

    return matrices_with_all_column_combinations_negated


def main():
    matrices_with_all_column_combinations_negated = generate_negated_column_combinations(recover_working_eight_by_sixteens()) # or enter another list of numpy matrices here
        
    with open("negated_combinations.pickle", "wb") as f:
        pickle.dump(matrices_with_all_column_combinations_negated, f)
        
    with open("negated_combinations.txt", "w+") as f:
        for matrix_with_negated_columns in matrices_with_all_column_combinations_negated:
            f.write(numpy_matrix_pretty(matrix_with_negated_columns) + "\n\n")
    

if __name__ == "__main__":
    main()
