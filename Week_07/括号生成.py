class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def DFS(left, right, tmp):
            # terminator
            if left == n and right == n:
                res.append(tmp)
                return
            # process current level & drill down
            if left < n:
                DFS(left + 1, right, tmp + '(')
            if right < left:
                DFS(left, right + 1, tmp + ')')
            # str is immutable, no need to reset states
        res = []
        DFS(0, 0, '')
        return res
