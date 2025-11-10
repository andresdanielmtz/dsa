# Breath First Search Applied 
from queue import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None

# while there's at least one value in the queue, keep on iterating

def bfs(tree: list[Node]):
    if not tree: return # If there's no tree, just return to how it was.
    queue = deque()
    queue.append(tree.pop())

    # while the queue is still on works.
    while queue:
        print(f"curr val: {queue[0]}")