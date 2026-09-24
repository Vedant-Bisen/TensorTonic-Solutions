import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here

    def actual_fn(x):
        return 1/(1 + np.exp(-x))
        
    if type(x) == float:
        actual_fn(x)

    x_array = np.array(x)
    return actual_fn(x_array)