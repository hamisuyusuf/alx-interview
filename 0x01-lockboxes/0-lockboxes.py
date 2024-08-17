#!/usr/bin/python3
"""
Module 0-lockboxes
This module contains the canUnlockAll function, which determines
if all the boxes in a list can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    Parameters:
        boxes (list of lists): A list where each element is a list of keys
                               available in that box.
    
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = set([0])  # Set to keep track of opened boxes, starting with box 0
    keys = set(boxes[0])  # Collect keys from the first box (which is already open)
    
    while keys:
        key = keys.pop()  # Remove a key from the set
        if key < n and key not in opened:
            opened.add(key)  # Mark the box corresponding to the key as opened
            keys.update(boxes[key])  # Add new keys found in the newly opened box
    
    return len(opened) == n  # Return True if all boxes are opened, else False
