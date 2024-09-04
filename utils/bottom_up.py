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

def matrix_chain_path(d):
    '''
    Returns the minimum number of multiplications needed to multiply the matrices in the chain
    and the optimal parenthesization directly during the bottom-up dynamic programming approach.
    
    Parameters:
      d: list of integers representing the dimensions of the matrices in the chain.
      
    Returns:
      cost: The minimum number of multiplications needed to multiply the matrices in the chain.
      order: The optimal order of matrix multiplication.
    '''
    
    n = len(d)
    
    # Will store the minimum number of multiplications needed to multiply the matrices in the chain.
    registry = np.zeros((n, n))
    
    # order[i][j] will hold the optimal order of matrix multiplication from i to j
    order = [["" for _ in range(n)] for _ in range(n)]
    
    # Initialize the order for single matrices (base case)
    for i in range(1, n):
      order[i][i] = f"A{i}"

    # Check for subsets of size 2 (minimum size for multiply) to n (maximum size).
    for subset in range(2, n):  
      for i in range(1, n - subset + 1):  
        j = i + subset - 1
        registry[i][j] = np.inf
        
        # Try all possible positions to split the matrix chain
        for k in range(i, j):
          # Compute the cost of splitting the matrices at position k
          cost = registry[i][k] + registry[k + 1][j] + d[i - 1] * d[k] * d[j]
          
          # Update the minimum cost and the order if a new minimum is found
          if cost < registry[i][j]:
            registry[i][j] = cost
            # The optimal order is the order of the left partition followed by the order of the right partition
            order[i][j] = f"({order[i][k]} x {order[k + 1][j]})"
    
    # The result for the full chain (from matrix 1 to matrix n-1) is in registry[1][n-1]
    # The optimal order is stored in order[1][n-1]
    return registry[1][n-1], order[1][n-1]
