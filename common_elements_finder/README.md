# Common Elements Finder

## Task

Write a program to find and display the common elements between two lists of integers. It must take two lists as input and return a new list containing the common elements.

## Usage

### Input Format

- The input consists of two lines:
  1. The first line contains space-separated integers representing the elements of the first list.
  2. The second line contains space-separated integers representing the elements of the second list.

### Output Format

- A single line containing space-separated integers representing the common elements between the two input lists. The elements appear in the same order as they appear in the first list.

### Example

**Input:**

```
1 2 3 4 5
3 4 5 6 7
```

**Output:**

```
3 4 5
```

## Constraints

- The input lists may have at most 10^5 elements each.
- The input integers are in the range [-10^9, 10^9].

## How It Works

1. The program first creates a set from the second list for efficient element lookup.
2. It initializes an empty list to store common elements.
3. Then, it iterates through the first list, checking if each element is in the set created from the second list.
4. Common elements are added to the `common_elements` list.
5. Finally, the program prints the common elements.

## Solution: 
This is the solution for the following question: https://github.com/itzsshashank/Python_Mini_Questions/blob/main/common_elements_finder/common_elements_finder.py
