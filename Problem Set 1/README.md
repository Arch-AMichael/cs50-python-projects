# Problem Set 1 – Conditionals (CS50’s Introduction to Programming with Python)

This folder contains my solutions to Problem Set 1.  
The programs focus on **conditional logic, string handling, and basic math operations** in Python.

---

## Problems

### 1. Deep Thought (`deep.py`)
- Prompts the user for the “answer to the Great Question of Life, the Universe, and Everything.”  
- Accepts variations of **42**, including:
  - `42`
  - `forty-two`
  - `forty two`  
- Outputs **Yes** if the answer matches; otherwise outputs **No**.

---

### 2. Home Federal Savings Bank (`bank.py`)
- Prompts the user for a greeting.  
- Outputs based on greeting:
  - Starts with `"hello"` → `$0`
  - Starts with `"h"` (but not `"hello"`) → `$20`
  - Anything else → `$100`  
- Ignores leading whitespace and treats input case-insensitively.

---

### 3. File Extensions (`extensions.py`)
- Prompts for a filename and outputs the corresponding **MIME type**.  
- Recognized extensions:
  - `.gif` → `image/gif`
  - `.jpg` / `.jpeg` → `image/jpeg`
  - `.png` → `image/png`
  - `.pdf` → `application/pdf`
  - `.txt` → `text/plain`
  - `.zip` → `application/zip`
- All other or missing extensions → `application/octet-stream`.

---

### 4. Math Interpreter (`interpreter.py`)
- Prompts for an arithmetic expression in the form `x y z` (e.g., `3 * 4`).  
- Supports operators: `+`, `-`, `*`, `/`.  
- Outputs the result as a floating-point value with **1 decimal place**.  
- Example:  
  - Input: `7 / 2`  
  - Output: `3.5`

---

### 5. Meal Time (`meal.py`)
- Prompts for a time in **24-hour format** (`#:##` or `##:##`).  
- Determines the current meal based on the time:
  - 7:00–8:00 → **Breakfast**
  - 12:00–13:00 → **Lunch**
  - 18:00–19:00 → **Dinner**
- Uses a helper function `convert(time: str) -> float` to convert input time into hours as a float (e.g., `"7:30"` → `7.5`).

---

## Skills Practiced
- Conditional statements (`if`, `elif`, `else`)
- String comparison and case handling
- Type conversion between strings, integers, and floats
- Basic parsing and interpretation of user input
- Structuring code with helper functions
