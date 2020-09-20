class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.aux(root, result)
        return result

    def aux(self, root, result):
        if root:
            result.append(root.val)
            if root.children:
                for child in root.children:
                    self.aux(child, result)
