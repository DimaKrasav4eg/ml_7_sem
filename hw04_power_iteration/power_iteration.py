import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    
    r = np.random.rand(data.shape[1])
    for i in range(num_steps):
        Ar = data.dot(r)
        r = Ar / np.linalg.norm(Ar)
    lamb = float(r.dot(data).dot(r)/r.dot(r))
    return (lamb, r)