class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i, n in enumerate(nums):
            if target - n in hashMap.keys():
                return [hashMap[target - n], i]
            hashMap[n] = i