class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def parent(i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                p[i], i = root, p[i]
            return root
        
        def union(count, i, j):
            pi = parent(i)
            pj = parent(j)
            if pi == pj:
                return count
            p[pi] = pj
            return count - 1

        n = len(M)
        p = [i for i in range(n)]
        count = n
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    count = union(count, i, j)
        return count
