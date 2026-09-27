# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
        # original_range = set(range(0, len(nums)))
        # nums_set = set(nums)
        # missing_num = original_range - nums_set
        # return list(missing_num)[0]

a = Solution()
print(a.missingNumber([3,0,1]))
