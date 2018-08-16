# Problem

This problem was asked by Facebook.

There is an N by M matrix of zeroes.
Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner.
You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2,
since there are two ways to get to the bottom-right:

- Right, then down
- Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

# Solutions

https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/

## Brute force

=> The time complexity of above recursive solution is exponential.

## Dynamic Programming

So this problem has both properties (see this and this) of a dynamic programming problem.
Like other typical Dynamic Programming(DP) problems, recomputations of same subproblems can be avoided by constructing a temporary array count[][] in bottom up manner using the above recursive formula.

=> Time complexity of the above dynamic programming solution is O(mn).

## Direct formula: Combinations

Note the count can also be calculated using the formula (m-1 + n-1)!/(m-1)/!(n-1)!.