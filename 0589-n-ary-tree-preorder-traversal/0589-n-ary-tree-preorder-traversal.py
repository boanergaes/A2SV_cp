"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            if not root:
                return

            track.append(root.val)
            for child in root.children:
                dfs(child)

        track = []
        dfs(root)
        return track