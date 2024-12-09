class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        if nums_len == 2:
            return [0,1]
        for i in range(0, nums_len):
            for j in range(i+1, nums_len):
                if nums[i]+nums[j] == target:
                    return [i,j]
                    break