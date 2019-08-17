from typing import Callable

# First implement a gradient checker by filling in the following functions
def gradcheck_numeric(cost: Callable, grad: Callable, x: np.ndarray):
    """
    cost - cost function
    grad - cost function gradients
    x -- the point (numpy array) to check the gradient at
    """
    fx = cost(x)    # Evaluate cost
    grads = grad(x) # Evaluate grads
    h = 1e-4        # Offset to calculate central difference
    prec = 1e-5     # Max relative difference for numerical computations
    
    assert x.dtype.kind == 'f' # we need float data

    # Iterate over all indexes ix in x to check the gradient.
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        ix = it.multi_index

        ### YOUR CODE HERE:
        num_x = x.copy()
        
        # back
        num_x[ix]  = x[ix] - h
        cost_back  = cost(num_x)
        
        # front
        num_x[ix]  = x[ix] + h 
        cost_front = cost(num_x)
        
        numgrad = (cost_front - cost_back) / (2 * h)
        ### END YOUR CODE

        # Compare gradients
        reldiff = abs(numgrad - grads[ix]) / max(1, abs(numgrad), abs(grads[ix]))
        if reldiff > 1e-5:
            print ("Gradient check failed.")
            print ("First gradient error found at index %s" % str(ix))
            print ("Your gradient: %f \t Numerical gradient: %f" % (
                grads[ix], numgrad))
            return

        it.iternext() # Step to next dimension

    print ("Gradient check passed!")