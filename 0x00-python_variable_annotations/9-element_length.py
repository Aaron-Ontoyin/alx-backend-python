#!/usr/bin/env python3
"""Let's duck type an iterable object"""
from typing import List, Any, Tuple


def element_length(lst: List[List[Any]]) -> List[Tuple[List[Any], int]]:
    """Gets elements and their lens"""
    return [(i, len(i)) for i in lst]
