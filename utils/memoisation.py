import numpy as np

def matrix_chain(d):
  '''
  Returns the minimum number of multiplications needed to multiply the matrices in the chain.
  
  Parameters:
    d: list of integers representing the dimensions of the matrices in the chain.
    
  Returns:
    cost: The minimum number of multiplications needed to multiply the matrices in the chain.
  '''
  
  # Memory uses a dictionary to facilitate matrix memory access. Starts empty as no value has been calculated.
  mem = {}
  return _matrix_chain_mem(1, len(d) - 1, d, mem)

def _matrix_chain_mem(i, j, d, mem):
  '''
  Returns the minimum number of multiplications needed to multiply a subset of matrices in the chain, recursively.
  
  Parameters:
    i: The index of the first matrix in the subset.
    j: The index of the last matrix in the subset.
    d: list of integers representing the dimensions of the matrices in the chain.
    mem: dictionary to store the memoized values.
  
  Returns:
    min_cost: The minimum number of multiplications needed to multiply the matrices in the subset.
  '''
  
  # Checks for memoized value
  if (i, j) in mem:
    return mem[(i, j)]
  
  # Base case
  if i == j:
    return 0
  
  # Initialize minimum cost to infinity to ensure that the first cost calculated is less than it.
  min_cost = np.inf
  
  for k in range(i, j):
    # Calculate the cost of multiplying the matrices in the subset.
    cost = (
        _matrix_chain_mem(i, k, d, mem) + 
        _matrix_chain_mem(k + 1, j, d, mem) + 
        d[i - 1] * d[k] * d[j]
      )
    
    # Update the minimum cost.
    if cost < min_cost:
      min_cost = cost
  
  mem[(i, j)] = min_cost
  
  return mem[(i, j)]
  