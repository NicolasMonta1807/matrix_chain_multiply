from utils import recursive, memoisation
import time

def main():
    d = [5, 4, 6, 2, 7]
    
    start = time.perf_counter_ns()
    rec_sol = recursive.matrix_chain(d)
    end = time.perf_counter_ns()
    print("Recursive solution: ", rec_sol)
    print("Time taken: ", end - start, " ns")

if __name__ == "__main__":
    main()