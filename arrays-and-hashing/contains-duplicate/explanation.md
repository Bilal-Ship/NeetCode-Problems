# Contains Duplicate

## Problem

Given an integer array `nums`, return `true` if any value appears more than once in the array. Otherwise, return `false`.

## Examples

### Example 1

```python
Input: nums = [1, 2, 3, 3]
Output: True
```

### Example 2

```python
Input: nums = [1, 2, 3, 4]
Output: False
```

## Constraints

```txt
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
```

## Pattern

Arrays & Hashing

## Difficulty

Easy

---

## Solution

[View my solution.py file](solution.py)

---

## Explanation

The goal is to check whether any number appears more than once in the array.

My solution uses a set called `parsed` to store every number that has already been seen while looping through `nums`.

At the start, I assume there are no duplicates.

Then, for each number in `nums`, I check whether that number is already inside `parsed`.

If it is already in `parsed`, that means the number appeared before, so the array contains a duplicate.

If it is not in `parsed`, I add it to the set and continue checking the rest of the array.

At the end, the solution returns whether a duplicate was found.

---

## Why This Works

A set allows fast lookup.

Instead of comparing every number with every other number, I only check whether the current number has already appeared before.

If a number appears twice, the second time it appears, it will already be inside the set.

That is how the duplicate is detected.

---

## Time Complexity

```txt
O(n)
```

The algorithm loops through the array once.

Set lookup and set insertion are O(1) on average.

Therefore, the total time complexity is O(n).

---

## Space Complexity

```txt
O(n)
```

In the worst case, every number is unique, so the set may store all `n` numbers.

Therefore, the space complexity is O(n).

---


## Note

My solution works, but the extra `duplicate` set is not needed because the problem only asks whether a duplicate exists, not which values are duplicated.



---

## Edge Cases

- Empty array
- Array with one element
- All numbers are unique
- Duplicate appears near the beginning
- Duplicate appears near the end
- Negative numbers
- Very large numbers

---
