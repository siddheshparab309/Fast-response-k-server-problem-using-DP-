# Project: Fast Response k-Server Problem – Dynamic Programming & Runtime Analysis

**Author:** Aryan Saxena, Siddhesh Parab, Nithin Maheshwarappa and Christabell Rego. 
**Purpose:** Implement and analyze a dynamic programming algorithm for the Fast Response k-Server Problem on a linear network. The program computes optimal server placements, measures experimental runtime for various input sizes, compares results with the theoretical time complexity, and visualizes both curves.

---

## Files Included

1. **k-server.py**  
   - Complete Python implementation of the project.  
   - Precomputes segment costs, runs the DP algorithm, and records normalized cost and runtime for multiple values of *n*.  
   - Generates a plot comparing experimental runtime with the scaled theoretical \( n^2 \) curve.

2. **requirements.txt**  
   - Contains required Python library (`matplotlib`).  

---

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Experiment
```bash
python k-server.py
```

### Output
The script prints:
```
n =  20 | Normalized Cost = 1.6239 | Runtime = 0.438 ms
n =  40 | Normalized Cost = 3.3251 | Runtime = 1.652 ms
...
n = 200 | Normalized Cost = 16.4660 | Runtime = 41.375 ms
```

It also shows a plot with:
- **Experimental runtime** (solid line)  
- **Scaled theoretical runtime (n²)** (dashed line)  
- **X-axis:** number of clients  
- **Y-axis:** runtime in milliseconds  

---

## Purpose of This Project

### Theoretical Analysis
- Clients lie on a line ⇒ optimal placement divides them into **k contiguous segments**.  
- Best server location for a segment \([l, r]\) is the **weighted median** of that segment.  
- Segment cost precomputation: \( O(n^2) \).  
- DP recurrence:
  \\[
  DP[i][j] = \min_{t < i}\big( DP[t][j-1] + Cost(t+1, i) \big)
  \\]
- Total time complexity: **\( O(n^2 k) \)**.

### Experimental Validation
- Runs DP for \( n = 20, 40, ..., 200 \).  
- Records normalized cost and runtime.  
- Computes theoretical values proportional to \( n^2 \) and scales them to match the first experimental point.  
- Combined graph confirms expected performance trend.

---

## Conclusions
- DP correctly finds optimal server placements for each value of *n*.  
- Experimental runtime shows clear quadratic growth, matching the theoretical \( O(n^2 k) \) complexity.  
- The scaled theoretical curve closely tracks the experimental curve.  
- Minor runtime noise is expected due to Python interpreter overhead and system variation.

---

## GitHub Code Repository
The complete project can be found at:  
https://github.com/ari-sax/Fast-Rsponse-k-Server-Problem-using-DP-.git

---

## Notes
- Random weights simulate varying client traffic.  
- Normalized cost = (optimal DP cost) ÷ (total traffic).  
- Theoretical runtime is scaled only to allow visual comparison.  
- Runtime may vary slightly depending on system performance.
