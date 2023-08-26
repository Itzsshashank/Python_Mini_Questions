## Cartesian Product ( Itertools Product)
This tool computes the [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

## Question
You are given a two lists A and B. Your task is to compute their cartesian product AXB.
'''A = [1, 2]
   B = [3, 4]

  AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.
