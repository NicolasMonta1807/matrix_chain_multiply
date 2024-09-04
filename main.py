from utils import recursive, memoisation, bottom_up
import time

def main():
    d = [10, 20, 30, 40]
    
    start = time.perf_counter_ns()
    rec_sol = recursive.matrix_chain(d)
    end = time.perf_counter_ns()
    print("Recursive solution: ", rec_sol)
    print("Time taken: ", end - start, " ns")
    
    start = time.perf_counter_ns()
    mem_sol = memoisation.matrix_chain(d)
    end = time.perf_counter_ns()
    print("Memoisation solution: ", mem_sol)
    print("Time taken: ", end - start, " ns")
    
    start = time.perf_counter_ns()
    bu_sol = bottom_up.matrix_chain(d)
    end = time.perf_counter_ns()
    print("Bottom-up solution: ", bu_sol)
    print("Time taken: ", end - start, " ns")
    
    start = time.perf_counter_ns()
    bu_sol_analysis, order = bottom_up.matrix_chain_path(d)
    end = time.perf_counter_ns()
    print("Bottom-up solution with mem-analysis: ", bu_sol_analysis, "\n\t - Solution path: ", order)
    print("Time taken: ", end - start, " ns")
    

if __name__ == "__main__":
    main()