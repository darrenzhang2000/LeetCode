# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, curH=0):
            if not node:
                return
            nonlocal height
            height = max(height, curH + 1)
            helper(node.left, curH + 1)
            helper(node.right, curH + 1)
        height = 0
        helper(root)
        res = [[] for _ in range(height)]
        def removeLeafs(node):
            if not node:
                return -1
            leftH = removeLeafs(node.left)
            rightH = removeLeafs(node.right)
            
            curH = max(leftH, rightH) + 1
            res[curH].append(node.val)
            return curH
            
        removeLeafs(root)
        return res
