class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_diff, xy_sum):
            # terminator
            if len(queens) == n:
                res.append(queens)
                return
            p = len(queens)
            for q in range(n):
                if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                    DFS(queens + [q], xy_diff + [p-q], xy_sum + [p+q])
        res = []
        DFS([], [], [])
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in sol] for sol in res]
