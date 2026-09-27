# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        hash = {value:i for i,value in enumerate(nums)}
        for i,value in enumerate(nums):
            if target - value in hash:
                if i == hash[target - value]:continue
                else: return i , hash[target - value]


test_case = {
    'case1':[[2,7,11,15],9],
    'case2':[[3,2,4],6],
    'case3':[[3,3],6]
}

a = Solution()
print(a.twoSum(test_case['case3'][0],test_case['case3'][1]))