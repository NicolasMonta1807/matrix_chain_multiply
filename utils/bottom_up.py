import numpy as np

def matrix_chain(d):
  '''
  Returns the minimum number of multiplications needed to multiply the matrices in the chain.
  
  Parameters:
    d: list of integers representing the dimensions of the matrices in the chain.
    
  Returns:
    cost: The minimum number of multiplications needed to multiply the matrices in the
  '''
  
  
  n = len(d)
  
  # Will store the minimum number of multiplications needed to multiply the matrices in the chain.
  registry = np.zeros((n, n))
  
  # Check for subsets of size 2 (minimum size for multiply) to n (maximum size).
  for subset in range(2, n):
    
    # Check for all possible subsets of size subset.
    for i in range(1, n - subset + 1):
      j = i + subset - 1
      
      # Initialize the minimum cost to infinity to ensure that the first cost calculated is less than it.
      registry[i][j] = np.inf
      
      # Check for all possible partitions of the subset.
      for k in range(i, j):
        cost = (
              registry[i][k] + 
              registry[k + 1][j] + 
              d[i - 1] * d[k] * d[j]
            )
        
        # Update the minimum cost.
        if cost < registry[i][j]:
          registry[i][j] = cost
  
  return registry[1][n - 1]