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

def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i - 1]:
            continue
        d = {}
        for x in nums[i + 1:]:
            if x not in d:
                d[-v - x] = 1
            else:
                res.add((v, -v - x, x))
    return map(list, res)


a = [-1, 0, 1, -4]
res = threeSum(a)
print([x for x in res])


def threeSum02(nums):
    """
    双指针解题
    :param nums:
    :return:
    """
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i >0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l<r:
            s = nums[i] + nums[l] + nums[r]
            if s<0: l+=1
            elif s >0: r-=1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l<r and nums[l] == nums[l+1]:
                    l +=1
                while l<r and nums[r] == nums[r-1]:
                    r -= 1
                l+=1; r-=1

def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
    n = len(nums)
    if n < 4: return []
    nums.sort()
    res = []
    for i in range(n - 3):

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 当数组最小值和都大于target 跳出
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        # 当数组最大值和都小于target,说明i这个数还是太小,遍历下一个
        if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
            continue
        for j in range(i + 1, n - 2):
            # 防止重复 数组进入 res
            if j - i > 1 and nums[j] == nums[j - 1]:
                continue
            # 同理
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            # 同理
            if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                continue
            # 双指针
            left = j + 1
            right = n - 1
            while left < right:
                tmp = nums[i] + nums[j] + nums[left] + nums[right]
                if tmp == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif tmp > target:
                    right -= 1
                else:
                    left += 1
    return res