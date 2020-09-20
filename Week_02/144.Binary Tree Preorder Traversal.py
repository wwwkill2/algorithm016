class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.aux(root, result)
        return result

    def aux(self, root, result):
        if root:
            result.append(root.val)
            self.aux(root.left, result)
            self.aux(root.right, result)
