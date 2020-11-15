class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(low, high):
            while low < high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        arr = list(s)
        i = 0
        while i < len(s):
            reverse(i, min(i+k-1, len(arr) - 1))
            i += k*2
        return ''.join(arr)
