class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postorder(node):
            if not node:
                return False

            leftContains1 = postorder(node.left)
            rightContains1 = postorder(node.right)
            if not leftContains1:
                node.left = None
            if not rightContains1:
                node.right = None
            return root.val or leftContains1 or rightContains1
        
        return root if postorder(root) else None
