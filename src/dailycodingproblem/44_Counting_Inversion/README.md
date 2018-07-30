# Problem

This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

# Solution

https://www.cp.eng.chula.ac.th/~piak/teaching/algo/algo2008/count-inv.htm

```
Algorithm to count inversion
Use divide and conquer

    divide: size of sequence n to two lists of size n/2
    conquer: count recursively two lists
    combine:  this is a trick part (to do it in linear time)

combine use merge-and-count.
Suppose the two lists are A, B.
They are already sorted.
Produce an output list L from A, B while also counting the number of inversions, (a,b) where a is-in A, b is-in B and a > b.

The idea is similar to "merge" in merge-sort.
Merge two sorted lists into one output list, but we also count the inversion.
```
