## [Itertools Permutatoin](https://docs.python.org/2/library/itertools.html#itertools.permutations)

This tool returns successive r length permutations of elements in an iterable.
If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.
Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

***

## Question
You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

***

### Input Format
A single line containing the space separated string S and the integer value k.
Constraints: ```0 < K ≤ len(s)```

The string contains only UPPERCASE characters.

### Output Format
Print the permutations of the string  on separate lines.

***

#### Sample Input
```RAM 2```

#### Sample Output
```
AM
AR
MA
MR
RA
RM
```

***

## Solution
The Solution for the following question is: https://github.com/itzsshashank/Python_Mini_Questions/blob/main/Itertools_product/itertools_product.py
