#!/usr/bin/env python3
"""Type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes floats list and return the sum as float"""
    a: float = 0.0
    for i in input_list:
        a += i
    return a
