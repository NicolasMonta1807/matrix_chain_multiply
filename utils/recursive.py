import numpy as np

def matrix_chain(d):
  '''
  Returns the minimum number of multiplications needed to multiply the matrices in the chain.
  
  Parameters:
    d: list of integers representing the dimensions of the matrices in the chain.
    
  Returns:
    cost: The minimum number of multiplications needed to multiply the matrices in the chain.
  '''
  return matrix_chain_aux(1, len(d) - 1, d)

def matrix_chain_aux(i, j, d):
  '''
  Returns the minimum number of multiplications needed to multiply a subset of matrices in the chain, recursively.
  
  Parameters:
    i: The index of the first matrix in the subset.
    j: The index of the last matrix in the subset.
    d: list of integers representing the dimensions of the matrices in the chain.
  
  Returns:
    min_cost: The minimum number of multiplications needed to multiply the matrices in the subset.
  '''
  if i == j:
    return 0
  
  # Minimum cost is initialized to infinity to ensure that the first cost calculated is less than it.
  min_cost = np.inf
  
  # Try all possible splits of the subset.
  for k in range(i, j):
    # Calculate the cost of multiplying the matrices in the subset.
    cost = matrix_chain_aux(i, k, d) + matrix_chain_aux(k + 1, j, d) + d[i - 1] * d[k] * d[j]
    # Update the minimum cost.
    if cost < min_cost:
      min_cost = cost
  
  return min_cost