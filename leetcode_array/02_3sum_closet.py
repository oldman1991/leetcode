#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/11/6


"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

>>> a = [-1,2,1,-4]
>>> three_sum_closet(a, 1)
2
"""


def three_sum_closet(nums, target):
    """

    :param nums: array[int]
    :param target: int target
    :return: int
    """
    nums.sort()
    if len(nums) < 3:
        return None
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            res = nums[i] + nums[j] + nums[k]
            if res == target:
                return res
            if abs(res - target) < abs(result - target):
                result = res
            if res > target:
                k -= 1

            else:
                j += 1
    return result
