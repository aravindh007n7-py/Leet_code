# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        output , identify_duplicate = [] , [False] * (len(nums)+1)
        for x in nums:
            identify_duplicate[x] = True
        for y in range(1,len(nums)+1):
            if not identify_duplicate[y]:
                output.append(y)
        return output



test_case = {'case 1':[4,3,2,7,8,2,3,1],
             'case 2':[1,1]
             }

a = Solution()
print(a.findDisappearedNumbers(test_case['case 1']))
