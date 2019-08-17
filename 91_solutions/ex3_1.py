def values_to_ohe(indices: list, depth: int):
    if max(indices) > depth-1:
        raise ValueError(f"Given vector of indices:'{indices}' contains " \
                         f"values beyond range (0, depth-1): (0,{depth-1})")
    ### INSERT YOUR CODE HERE ####
    result = np.eye(depth)[indices]
    ### STOP YOUR CODE HERE ####
    return result
