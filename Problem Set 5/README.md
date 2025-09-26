# Problem Set 5 – Unit Tests

This problem set focuses on **writing unit tests using `pytest`** to ensure programs behave as expected. Each problem reimplements a previous assignment but adds structured functions and test cases.

---

## Problems Included

### 1. Testing my twttr
- **Files:** `twttr.py`, `test_twttr.py`
- **Description:**  
  Reimplement the program that shortens words by omitting vowels (A, E, I, O, U).  
  - `shorten(word)` removes vowels and returns the modified string.  
  - `main()` handles user input/output.  
  - `test_twttr.py` contains unit tests to validate functionality.

---

### 2. Back to the Bank
- **Files:** `bank.py`, `test_bank.py`
- **Description:**  
  Reimplement the bank program that assigns a value to greetings.  
  - `value(greeting)` returns:
    - `0` if greeting starts with `"hello"`  
    - `20` if greeting starts with `"h"` (but not `"hello"`)  
    - `100` otherwise  
  - Case-insensitive, no leading spaces assumed.  
  - `test_bank.py` includes multiple test cases for edge scenarios.

---

### 3. Vanity Plates
- **Files:** `plates.py`, `test_plates.py`
- **Description:**  
  Reimplement vanity plate validation.  
  - `is_valid(s)` checks whether a plate string meets all given rules (length, letters, numbers, placement, etc.).  
  - `main()` runs only when executed directly.  
  - `test_plates.py` thoroughly tests valid and invalid plates.

---

### 4. Refueling
- **Files:** `fuel.py`, `test_fuel.py`
- **Description:**  
  Reimplement fuel gauge functionality.  
  - `convert(fraction)` converts fractions (`X/Y`) to a percentage, rounding to the nearest integer.  
    - Raises `ValueError` for invalid input or if `X > Y`.  
    - Raises `ZeroDivisionError` if denominator is `0`.  
  - `gauge(percentage)` returns:
    - `"E"` if ≤ 1%  
    - `"F"` if ≥ 99%  
    - `"{Z}%"` otherwise  
  - `test_fuel.py` includes tests for both conversion and gauge logic.

---

## How to Run Tests
To run all tests for this problem set:

```bash
pytest "file_name"

- for example: "pytest test_twttr.py"


