# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def recursiveFind(node, lv):
            nonlocal result
            if node is None:
                return
            if len(result) - 1 < lv:
                result.append([])
            
            result[lv].append(node.val)

            recursiveFind(node.left, lv+1)
            recursiveFind(node.right, lv+1)

        
        recursiveFind(root, 0)
        return result