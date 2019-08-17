def np_softmax(array: np.array, axis = -1):
    ### INSERT YOUR CODE HERE ###
    array = array - np.max(array, axis=axis, keepdims=True)
    array_exp = np.exp(array)
    result = array_exp / np.sum(array_exp, axis=axis, keepdims=True)
    ### STOP YOUR CODE HERE ###
    return result
