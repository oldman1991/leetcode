#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2018/11/6
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
>>> a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
>>> maxArea(a)
49
>>> maxArea02(a)
49
"""


def maxArea(height):
    """
    :param height: List[int]
    :return:
    """
    n = len(height)
    if n < 2:
        return 0
    max_value = 0
    for index, value in enumerate(height):
        for index_sec, value_sec in enumerate(height[index+1:]):
            area = (min(value, value_sec)) * (index_sec+1)
            if area > max_value:
                max_value = area
    return max_value

#
# a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# res = maxArea(a)
# print(res)


def maxArea02(height):
    """
    O(N)时间复杂度为n的算法
    :param height:  List[int]
    :return:
    """
    i = 0
    j = len(height) -1
    max_value = 0
    while i < j:
        max_value = max(max_value, (j-i)*min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_value


a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
res = maxArea02(a)
print(res)



