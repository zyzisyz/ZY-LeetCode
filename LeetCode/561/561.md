# [561. Array Partition I](https://leetcode.com/problems/array-partition-i/description/)

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

**Example 1:**

```
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
```

Note:

- n is a positive integer, which is in the range of [1, 10000].
- All the integers in the array will be in the range of [-10000, 10000].

---

## 数组分割

给了2n个整数，你的任务是把这些整数分为n组，例如 (a1, b1), (a2, b2), ..., (an, bn),可以让所有从1到n的min(ai, bi)的和尽可能的大。

例子1：

```
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
```

Note:

- n 是正整数，范围在 [1, 10000].
- 所有的整数范围是 [-10000, 10000].

## 思路

对数组排序，每最小的两个为一组

## C++

```
class Solution {
public:
   int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int sum = 0;
        for(int i = 0; i < nums.size(); i += 2) 
            sum += nums[i];
        return sum;
    }
};
```