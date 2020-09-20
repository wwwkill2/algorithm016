class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if not root:
            return result
        q = []
        q.append(root)
        self.aux(q, result)
        return result

    def aux(self, q, result):
        res = []
        nq = []
        for node in q:
            res.append(node.val)
            if node.children:
                nq.extend(node.children)
        result.append(res)
        if nq != []:
            self.aux(nq, result)
