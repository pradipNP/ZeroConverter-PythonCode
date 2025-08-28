# Number Printer

A simple Python project to print numbers based on whether the input `n` is positive or negative.

---

## Problem Link
This is a GeeksforGeeks problem:  
[Check the Status – GFG](https://www.geeksforgeeks.org/problems/check-the-status/1?page=1&category=python&sortBy=submissions)

---

## Problem Statement
- If `n` is **positive**, print numbers from `n-1` down to `0`.
- If `n` is **negative**, print numbers from `n` up to `0`.

---

## Previous Attempt (❌ Not Reliable)
```python
def pos(n):
    for i in range(n-1, 0, -1):
        print(i, end=" ")
    print(0)
    
def neg(n):
    for i in range(n, 1, 1): 
        print(i, end=" ")
```
Issue
- The above implementation fails for large inputs like 777, 4832, etc.
- For positive numbers, it may miss printing 0 correctly.
- For negative numbers, the range(n, 1, 1) loop does not include 0 and sometimes prints nothing at all.
