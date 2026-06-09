class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        mini = min(nums)
        return k * (maxi - mini)