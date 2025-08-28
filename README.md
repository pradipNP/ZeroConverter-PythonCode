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

## Correct Implementation (✅ Works for all inputs)
```python
def pos(n):
    n -= 1
    while n >= 0:
        print(n, end=' ')
        n -= 1

def neg(n):
    while n <= 0:
        print(n, end=' ')
        n += 1
```
Example
Input:
```ini
n = -3
```

Output:
```diff
-3 -2 -1 0
```
Usage
Run the program with Python:
```bash
python ZeroConverter.py
```
Example in code:
```python
pos(5)    # Output: 4 3 2 1 0
neg(-5)   # Output: -5 -4 -3 -2 -1 0
```
Requirements
- Python 3.10+

License
This project is licensed under the MIT License.
```pgsql

---

You can now **copy all of this** and paste it into a new `README.md` on GitHub or edit your existing one.  

Do you want me to also provide a **ready-to-copy `main.py` file with this explanation in comments** for your repo?


