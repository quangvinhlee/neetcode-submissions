class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in mp:
                return [mp[diff], index]

            mp[num] = index