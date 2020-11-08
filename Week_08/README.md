手写排序：
def bubble_sort(nums):
    if len(nums) < 2:
        return
    n = len(nums)
    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            break

def insert_sort(nums):
    if len(nums) < 2:
        return
    n = len(nums)
    for i in range(1, n):
        cur = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > cur:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = cur

def selection_sort(nums):
    if len(nums) < 2:
        return
    n = len(nums)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    
def merge_sort(nums):
    _merge_sort_between(nums, 0, len(nums)-1)

def _merge_sort_between(nums, low, high):
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort_between(nums, low, mid)
        _merge_sort_between(nums, mid+1, high)
        _merge(nums, low, mid, high)

def _merge(nums, low, mid, high):
    i, j = low, mid+1
    tmp = []
    while i <= mid and j <= high:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(nums[start:end+1])
    nums[low:high+1] = tmp

def quick_sort(nums):
    _quick_sort_between(nums, 0, len(nums)-1)

def _quick_sort_between(nums, low, high):
    if low < high:
        p = _partition(nums, low, high)
        _quick_sort_between(nums, low, p-1)
        _quick_sort_between(nums, p+1, high)

def _partition(nums, low, high):
    i = low
    for j in range(low, high):
        if nums[j] < nums[high]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i
