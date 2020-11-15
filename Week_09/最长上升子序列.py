class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                low, high = 0, len(d) - 1
                pos = 0
                while low <= high:
                    mid = (low + high) // 2
                    if d[mid] >= num:
                        loc = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                d[loc] = num
        return len(d)
