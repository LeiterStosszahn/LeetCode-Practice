class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        if nums_len == 2:
            return [0, 1]
        for i in range(0, nums_len):
            num_now = nums[i]
            num_need = target - num_now
            if num_need in nums:
                j = nums.index(num_need)
                if i != j:
                    return [i, j]