#!/usr/bin/env python3
"""
Type Checking Module. Advanced for function zoom Array
"""
from typing import Sequence, Generator, Any


def zoom_array(lst: Sequence[int], factor: int = 2) -> Sequence[Any]:
    """Zoom Array function: Zooms an array factor times"""
    zoomed_in: Sequence[Any] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array: Sequence[int] = [12, 72, 91]

zoom_2x: Sequence[Any] = zoom_array(array)

zoom_3x: Sequence[Any] = zoom_array(array, 3)
