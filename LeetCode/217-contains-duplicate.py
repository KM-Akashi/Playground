class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = set(nums)
        if len(count) < len(nums):
            return True
        return False
