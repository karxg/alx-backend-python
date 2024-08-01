#!/usr/bin/env python3
"""Type-annotated function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples int and sequence"""
    return [(i, len(i)) for i in lst]
