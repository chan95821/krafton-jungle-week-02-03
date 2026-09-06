# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, Tuple


class Solution:
    def recursiveFind(self, root=None)-> Tuple:
        if root is None:
            return -9000, -9000
        l_comprisable, l_incomprisable = self.recursiveFind(root.left)
        r_comprisable, r_incomprisable = self.recursiveFind(root.right)

        #  두 comprisable에 대해, 본인과 두 자식을 이은 결과 /한 comprisable에 대해 자식만 포함한 결과
        
        latter = l_comprisable + r_comprisable + root.val, l_comprisable, r_comprisable, l_incomprisable, r_incomprisable 
        #한 comprisable에 대해 본인과 자식을 이은 결과
        former = l_comprisable + root.val, r_comprisable + root.val, root.val

    
        return max(former), max(latter)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        a, b = self.recursiveFind(root)

        return max(a,b)
