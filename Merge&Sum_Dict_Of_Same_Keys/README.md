# Merge and Sum Dictionaries

## Problem Statement

You are given two dictionaries, `dict1` and `dict2`. Your task is to create a Python function to merge these dictionaries while summing the values for common keys.

## Input Format

- Two dictionaries, `dict1` and `dict2`, where each dictionary contains unique keys and non-negative integer values.
- The keys and values in the dictionaries can be of any valid data type for dictionaries.

## Output Format

- A dictionary, `merged_dict`, containing the merged result of `dict1` and `dict2`.

## Constraints

- The keys in the dictionaries are case-sensitive.
- The values in the dictionaries are non-negative integers.
- The keys and values can be of any valid data type for dictionaries.

## Example

```python
# Input the dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 10, 'c': 20, 'd': 30}

# Calling the function to merge dictionaries
result = merge_dictionaries(dict1, dict2)

print(result)
# Sample Output
# The merged dictionary will contain sum of values for common keys:
# {'a': 1, 'b': 12, 'c': 23, 'd': 30}
```

**Note:**

- The function `merge_dictionaries` should iterate through the input dictionaries and create a new dictionary containing the merged result. If a key exists in both dictionaries, the values should be summed.
- Ensure that the function handles cases where keys exist only in one of the dictionaries correctly.

## Solution:
The soultion ffor the aboove problem statement is: https://github.com/itzsshashank/Python_Mini_Questions/blob/main/Merge%26Sum_Dict_Of_Same_Keys/Merge%26Sum_Dict_Of_Same_Keys.py
