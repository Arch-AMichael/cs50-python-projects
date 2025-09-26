# Problem Set 3 – Exceptions

This problem set focuses on **handling errors and exceptions** in Python.  
Each exercise demonstrates how to validate user input, catch exceptions, and ensure programs behave correctly in unexpected scenarios.

---

## Problems

### 1. Fuel Gauge (`fuel.py`)
Prompts the user for a fraction **X/Y** representing fuel in a tank.  
- Outputs the tank’s fuel level as a **percentage (rounded)**.  
- Special cases:  
  - ≤ 1% → **E** (Empty)  
  - ≥ 99% → **F** (Full)  
- Re-prompts on invalid input (division by zero, non-integer values, numerator > denominator).  
- Demonstrates `try` / `except` with `ValueError` and `ZeroDivisionError`.

---

### 2. Felipe’s Taqueria (`taqueria.py`)
Simulates a **restaurant ordering system**.  
- Continuously prompts the user for menu items until **Ctrl-D** is pressed.  
- Displays the **running total** after each valid item, formatted as `$X.XX`.  
- Ignores invalid items and treats input case-insensitively.  
- Example:   
item: burrito
Total: $7.50



---

### 3. Grocery List (`grocery.py`)
Allows users to build a **grocery list**.  
- Accepts items until **Ctrl-D**.  
- Outputs the final list in:  
- **Uppercase**  
- **Alphabetical order**  
- With counts for duplicate items  
- Example:  
2 APPLES
1 BANANA


---

### 4. Outdated (`outdated.py`)
Converts U.S. dates into **ISO 8601 (YYYY-MM-DD)** format.  
- Accepts:  
- Numeric format → `MM/DD/YYYY` (e.g., `9/8/1636`)  
- Written month format → `Month DD, YYYY` (e.g., `September 8, 1636`)  
- Re-prompts for invalid input.  
- Outputs properly zero-padded ISO format (e.g., `1636-09-08`).  

---

## Skills Practiced
- Using **`try/except` blocks** for error handling  
- Handling **ValueError** and **ZeroDivisionError**  
- Input validation and normalization  
- Exception-safe loops with re-prompting  
- String parsing and date reformatting  
