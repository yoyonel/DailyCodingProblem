# Problem

This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.


# Solution

https://www.quora.com/Given-an-integer-array-such-that-every-element-occurs-3-times-except-one-element-which-occurs-only-once-how-do-I-find-that-single-element-in-O-1-space-and-O-n-time-complexity

## Procedure
1) Convert each number to base-3. Let's say the longest number has k digits (in base-3)
2) for all k digits, sum up all of the digits in the kth slot, and then take the result modulo 3.

The resulting digits make up the element that only occurs once.

```
A simple way to understand this algorithm is to imagine that you had a list of integers,
all but one of which are duplicated (instead of triplicated).
To find the lone number, you could just XOR all of the input numbers,
and then each number except for the lone number would be canceled out by its duplicate.
This is the same idea, except in base-3 instead of base-2.
```