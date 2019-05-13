#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/5/13


def lengthOfLongestSubstring( s: str) -> int:
    windows = []
    values = set()
    max_value = 0
    for i in s:
        if i not in values:
            windows.append(i)
            values.add(i)
        else:
            max_value = max(len(windows), max_value)
            while windows[0] != i:
                values.remove(windows[0])
                windows.pop(0)
            windows.pop(0)
            windows.append(i)
    return max(max_value, len(windows))

a = "abcabcbb"
print(lengthOfLongestSubstring(a))