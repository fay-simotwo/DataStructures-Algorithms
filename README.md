# Python Utility Functions

This repository contains three Python files that implement utility functions for common tasks:

1. `remove_duplicates.py`: This file contains a Python function that removes duplicate elements from a sequence (list or tuple) while preserving the original order of elements. It includes a test case to demonstrate its usage.

2. `stacks.py`: This file contains a Python function that checks if a given expression containing parentheses, curly braces, and square brackets is balanced (i.e., if each opening bracket has a corresponding closing bracket in the correct order). It also includes test cases to verify its correctness.

3. `word_frequency.py`: This file contains a Python function that calculates the frequency of each word in a sentence. It ignores punctuation and considers words in a case-insensitive manner. A test case is provided to showcase its functionality.

## Usage

You can use these utility functions in your Python projects by importing them as modules. Here's an example of how to use each function:

### Example Usage:

#### `remove_duplicates.py`

```python
from remove_duplicates import remove_duplicates

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
```

#### `stacks.py`

```python
from is_balanced import is_balanced

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

```

#### `word_frequency.py`

```python
from word_frequency import word_frequency

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

```

## Author
### Chepkoech Faith


## License
This project is licensed under MIT License.
