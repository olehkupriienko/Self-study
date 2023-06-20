def pivotIndex(self, nums: List[int]) -> int:
    if not nums:
        return -1
    total = sum(nums)
    left = 0
    for i in range(len(nums)):
        if left == total - left - nums[i]:
            return i
        left += nums[i]
    return -1