"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def recursive_construction(r_s, r_e, c_s, c_e):
            if r_e - r_s == 1:
                return Node(grid[r_s][c_s], True, None, None, None, None)

            before = grid[r_s][c_s]
            for i in range(r_s, r_e):
                for j in range(c_s, c_e):
                    if before != grid[i][j]:
                        mid_r = (r_s + r_e) // 2 # 항상 짝수
                        mid_c=  (c_s + c_e) // 2
                        return Node(True, False, 
                        recursive_construction(r_s,mid_r, c_s, mid_c), 
                        recursive_construction(r_s,mid_r, mid_c, c_e),
                        recursive_construction(mid_r, r_e, c_s, mid_c),
                        recursive_construction(mid_r, r_e, mid_c, c_e))
            
            return Node(grid[r_s][c_s], True, None, None, None, None)


        return recursive_construction(0, len(grid), 0, len(grid))            

