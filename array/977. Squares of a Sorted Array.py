# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

from collections import deque
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        answer = deque()
        l, r = 0, len(nums)-1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                answer.appendleft(left*left)
                l+=1
            else:
                answer.appendleft(right*right)
                r-=1
        return list(answer)

        
a = Solution()
print(a.sortedSquares([-7,-3,2,3,11]))