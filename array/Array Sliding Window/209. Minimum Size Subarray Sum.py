class Solution:
    def minSubArrayLen(self, target:int, nums:list[int])->int:
        l = 0
        total = 0  # to check whether we reach the target
        res = float('inf')  # to get the min subarray length

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(res, r-l+1)

                total -= nums[l]
                l += 1

        if res == float('inf'):
            return 0
        else:
            return res


a = Solution()
print(a.minSubArrayLen(target= 7, nums= [2,3,1,2,4,3,7]))



