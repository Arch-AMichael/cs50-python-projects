# Problem Set 6 – Unit Tests

This problem set focuses on **file handling, command-line arguments, data cleaning, CSV processing, image manipulation, and defensive programming** in Python. The exercises emphasize validating inputs, handling errors gracefully, and working with real-world file formats.

---

## Problems

### 1. Lines of Code
- **Files:** `lines.py`
- **Description:**  
  Counts the number of **lines of code (LOC)** in a Python file, excluding:
  - Blank lines  
  - Comment lines (lines starting with `#`, optionally preceded by whitespace)

  The program:
  - Accepts **exactly one** command-line argument: a `.py` file
  - Outputs the number of valid lines of code
  - Exits via `sys.exit` if:
    - Incorrect number of arguments
    - File does not end in `.py`
    - File does not exist

---

### 2. Pizza Py
- **Files:** `pizza.py`
- **Description:**  
  Reads a CSV file containing pizza menu data and displays it as a formatted **ASCII table** using the `tabulate` library.

  The program:
  - Accepts **exactly one** command-line argument: a `.csv` file
  - Uses `tabulate` with the **grid** format
  - Exits via `sys.exit` if:
    - Incorrect number of arguments
    - File does not end in `.csv`
    - File does not exist

---

### 3. Scourgify
- **Files:** `scourgify.py`
- **Description:**  
  Cleans and restructures student data from a CSV file by splitting names into first and last names.

  The program:
  - Reads an input CSV with columns: `name`, `house`
  - Writes a new CSV with columns: `first`, `last`, `house`
  - Accepts **exactly two** command-line arguments:
    - Input CSV file
    - Output CSV file
  - Exits via `sys.exit` if:
    - Incorrect number of arguments
    - Input file cannot be read

---

### 4. CS50 P-Shirt
- **Files:** `shirt.py`
- **Description:**  
  Overlays a transparent CS50 shirt image onto an input photo after resizing and cropping the image to fit.

  The program:
  - Accepts **exactly two** command-line arguments:
    - Input image (`.jpg`, `.jpeg`, or `.png`)
    - Output image (same extension as input)
  - Uses the `Pillow` library for image processing
  - Exits via `sys.exit` if:
    - Incorrect number of arguments
    - Invalid or mismatched file extensions
    - Input file does not exist

---

## Skills Practiced
- Command-line argument validation (`sys.argv`)
- File I/O and error handling
- CSV parsing with `csv.reader`, `DictReader`, and `DictWriter`
- Data cleaning and transformation
- Image processing with Pillow
- Defensive programming and graceful exits

---

## How to Run Tests

This problem set does **not** include automated unit tests.

All programs are executed directly from the command line using the required arguments.  
Each script validates input and exits gracefully using `sys.exit` when errors occur.
