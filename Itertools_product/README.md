## Cartesian Product [Itertools Product](https://docs.python.org/3/library/itertools.html)
This tool computes the [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

## Question
You are given a two lists A and B. Your task is to compute their cartesian product AXB.
```
EXAMPLE:
A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
```



Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format
The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.
Both lists have no duplicate integer elements.

Output Format
Output the space separated tuples of the cartesian product.

Sample Input:
```
1 2
3 4
```
 
```
Sample Output:
(1, 3) (1, 4) (2, 3) (2, 4)
```



## Solution
This is the solution for the following Questoion:
https://github.com/Itzsshashank/Python_Mini_Questions/blob/main/Itertools_product/itertools_product.py
