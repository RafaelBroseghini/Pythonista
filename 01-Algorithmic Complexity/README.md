# Notes on Algorithmic Complexity Analysis
1. A Data Structure refers to a **systematic way of organizing data**.
2. An algorithm **refers to the step by step procedure for perfoming a task in finite time.**

### First of all, why should we care?
1. Being able to measure an algorithm's efficiency (asymptotically) regardless of the hardware/software it runs in,
is an important process in designing an efficient algorithm.
2. We are often more concerned on how the algorithm's runtime increases as the size of input increases. Not in seconds, minutes
although these are good for benchmarks, but proportionally to input size.

### So how do we classify an algorithm as good?
1. We must have precise ways of calculating it's runtime and space usage.

### Runtime may vary according to:
1. Input size.
2. Computational resources.

### Best Case, Average Case, Worst Case
* Setting a standard for an algorithm to perform well at the worst case scenario
will ultimately design an algorithm that performs well on any input size.
* All that is required is to be able to identify the worst case and go from there.

### Time Complexities
| Time Complexity | Name |
| --------------- | ---- |
| O(1) | Constant
| O(logN) | Logarithmic ( x = logbN iff b^x = n)
| O(N) | Linear
| O(N log N) | Log Linear
| O(N^2) | Quadratic
| O(N^3) | Cubed
| O(base^n) | Exponential
| O(n!) | Factorial 

### Why do we use base 2 for logN?
* Computers store information in binary, therefore we simply omit log2N -> logN.
* It is also done through ceiling as the true log of a number requires calculus proofing, for algorithmic analysis purposes we are satisfied with the closest value to log.

Example: log2(12) = (12/2)/2)/2)/2) = (0.75 <= 1) log2(12) = 4

### Ideal Scenarios:
* Data Structures: O(1), O(logN)
* Algorithms: O(logN), O(N), O(N log N )

### Rules and tips when evaluating Asymptotic Analysis
* **Be aware if inputs sizes differ.** A nested loop with A elements iterating over B elements is not O(n^2) but, O(A*B).
* **Drop non dominant terms and constants.**
    * O(N) + O(logN) + 5 = O(N)
* **Describe in the simplest terms.**
* **Be aware of space complexity as well. It is common to trade time for space when designing an algorithm.**
  * Hash Tables!
