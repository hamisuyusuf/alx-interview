def canUnlockAll(boxes):
    n = len(boxes)
    opened = set([0])  # Start with the first box unlocked
    keys = set(boxes[0])  # Get keys from the first box
    
    while keys:
        key = keys.pop()  # Take one key from the set
        if key < n and key not in opened:
            opened.add(key)  # Mark the box corresponding to the key as opened
            keys.update(boxes[key])  # Add new keys found in the newly opened box
    
    return len(opened) == n  # Check if all boxes are opened
