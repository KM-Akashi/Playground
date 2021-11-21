class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = nums[0]
        for num in nums[1:]:
            temp = temp ^ num
        return temp
