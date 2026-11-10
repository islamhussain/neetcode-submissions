class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in d and i != d[n]:
                return [i, d[n]]