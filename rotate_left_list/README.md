**Problem Statement:**

You are tasked with implementing a Python function that rotates a given list to the left by a specified number of positions.

**Function Signature:**

```python
def rotate_left(lst, positions):
    pass
```

**Input:**

- `lst` (list of integers): The input list of integers to be rotated.
- `positions` (integer): The number of positions to rotate the list to the left.

**Output:**

- A new list containing the elements of the input list rotated to the left by the specified number of positions.

**Constraints:**

- The input list `lst` will contain at least one element.
- The number of positions `positions` is a non-negative integer.
- The length of `lst` will not exceed 10^5 elements.
- The integers in `lst` are within the range [-10^9, 10^9].

**Example:**

```python
# Input
original_list = [1, 2, 3, 4, 5]
positions_to_rotate = 2

# Output
rotated = rotate_left(original_list, positions_to_rotate)

# Sample Output
print(rotated)
# Output: [3, 4, 5, 1, 2]
```

**Context:**

In various scenarios, it's necessary to rotate a list to the left by a certain number of positions. This operation is commonly used in tasks like shifting elements in an array or reordering data. The `rotate_left` function is designed to accomplish this task efficiently by slicing and reordering the elements.
