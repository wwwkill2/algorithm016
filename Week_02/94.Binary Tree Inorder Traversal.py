class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.aux(root, result)
        return result

    def aux(self, root, result):
        if root:
            self.aux(root.left, result)
            result.append(root.val)
            self.aux(root.right, result)
