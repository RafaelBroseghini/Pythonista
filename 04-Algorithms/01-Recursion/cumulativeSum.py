#!/usr/bin/env python

"""
Given a number calculate
it's cumulative sum. From n to 0.
"""


def cumulative_sum(num):
    if num == 0:
        return 0
    else:
        return num + cumulative_sum(num - 1)


assert cumulative_sum(10) == 55
