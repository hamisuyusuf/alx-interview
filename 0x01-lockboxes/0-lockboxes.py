#!/usr/bin/env python3
from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists, where each inner list contains
        keys that can open other boxes.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]

    while keys:
        new_key = keys.pop()
        if 0 <= new_key < n and not opened[new_key]:
            opened[new_key] = True
            keys.extend(boxes[new_key])

    return all(opened)
