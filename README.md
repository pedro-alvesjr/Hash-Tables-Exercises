# 📚 Python Exercises – Duplicates in Lists

This repository contains simple solutions to logic problems using Python. The first exercises implement functions to handle common operations with lists and strings.

### 🔍 Current Exercises

**`find_duplicates(nums)`**  
This function takes a list of numbers (`nums`) and returns a new list containing only the numbers that appear more than once.

#### Example:

from duplicates import find_duplicates

print(find_duplicates([1, 2, 2, 3, 1, 4]))  # Output: [1, 2]

---

**`first_non_repeating_char(string)`**  
This function takes a string and returns the first character that does not repeat. If all characters repeat, it returns `None`.

#### Example:
from duplicates import first_non_repeating_char

print(first_non_repeating_char("aabbcdd"))  # Output: "c"
print(first_non_repeating_char("aabbcc"))   # Output: None

**`two_sum(nums, target)`**  
This function takes a list of numbers (`nums`) and a target value (`target`). It returns the indices of the two numbers in the list that add up to the target. If no such pair exists, it returns an empty list.

#### Example:
from duplicates import two_sum

print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sum([1, 2, 3], 7))       # Output: []


### Current Structure

├── duplicates.py       # File with the implemented functions
├── README.md           # This file

### Next Steps

- Add more functions and exercises.
- Organize by category (lists, dictionaries, strings, etc.).
- Write automated tests for the exercises.

### Requirements

- Python 3.6 or higher

### Contributions

Suggestions, improvements, and new exercises are welcome!
