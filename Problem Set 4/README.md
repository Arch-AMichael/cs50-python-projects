# Problem Set 4 – Libraries

This problem set focuses on **working with Python libraries** and external modules.  
Each exercise emphasizes using built-in and third-party libraries to extend Python’s functionality, from text formatting to APIs.

## Problems

### 1. Emojize (`emojize.py`)
- Prompts the user for a string.  
- Converts any **emoji codes/aliases** (e.g., `:thumbs_up:` or `:thumbsup:`) into actual emoji characters.  
- Uses the `emoji` library for text replacement.  

---

### 2. Frank, Ian and Glen’s Letters (`figlet.py`)
- Uses the **`pyfiglet` library** to render text in ASCII art fonts.  
- Command-line usage:
  - **Zero arguments** → Random font.  
  - **Two arguments** → `-f` or `--font` followed by the font name.  
- Prompts the user for text input and prints it in the chosen style.  
- Exits with an error message if arguments are invalid.  

---

### 3. Adieu, Adieu (`adieu.py`)
- Prompts the user for **names (one per line)** until `Ctrl-D`.  
- Outputs a farewell message formatted with correct English grammar:  
  - 1 name → `Adieu, adieu, to Liesl`  
  - 2 names → `Adieu, adieu, to Liesl and Friedrich`  
  - 3+ names → Uses commas and “and” appropriately.  
- Uses the **`inflect` library** to handle list formatting.  

---

### 4. Guessing Game (`game.py`)
- A number guessing game.  
- User provides a **level (n)** → program generates a random integer between 1 and *n*.  
- Prompts the user to guess:
  - Too small → `Too small!`  
  - Too large → `Too large!`  
  - Correct → `Just right!` and exits.  
- Validates inputs with re-prompts for non-integers.  
- Uses Python’s built-in `random` library.  

---

### 5. Little Professor (`professor.py`)
- Math quiz program inspired by the “Little Professor” toy.  
- User selects a **difficulty level (1, 2, or 3)**.  
- Generates **10 random addition problems** with numbers of that digit-length.  
- For each problem:
  - User has up to **3 tries**.  
  - Wrong input/answer → `EEE`.  
  - After 3 wrong tries → shows correct answer.  
- At the end → displays total **score out of 10**.  
- Uses helper functions:
  - `get_level()` → returns valid difficulty.  
  - `generate_integer(level)` → returns a random number with `level` digits.  

---

### 6. Bitcoin Price Index (`bitcoin.py`)
- Command-line program that takes a **number of Bitcoins** as an argument.  
- Fetches the **current Bitcoin price** (USD) from the **CoinCap API**.  
- Handles errors with `try/except` and `requests.RequestException`.  
- Outputs the cost in USD with proper formatting:  
  - Example: `$97,845.0243`  
- Uses the `requests` library for API calls.  

---

## Skills Practiced
- Using **third-party libraries** (`emoji`, `pyfiglet`, `inflect`, `requests`).  
- Command-line argument parsing with `sys.argv`.  
- Input validation and exception handling.  
- Random number generation with `random`.  
- Working with **APIs** and JSON data.  
- String formatting and user-friendly output.  
