# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         triplets = []
#         for index , value in enumerate(nums):
#             if (index > 0) & (value == nums[index - 1]):
#                 continue

#             left = index + 1
#             right = len(nums) - 1
#             while left < right:
#                 current_sum = value + nums[left] +nums[right]
#                 if current_sum > 0:
#                     right -= 1
#                 elif current_sum < 0:
#                     left += 1
#                 else:
#                     triplets.append([value,nums[left],nums[right]])
#                     left += 1

#                     while (left < right) & (nums[left] == nums[left - 1]):
#                         left += 1

#         return triplets

class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):
            print(f'The outer Loop i , n is {i} and {n}')

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            print(f' The value of j is {j} and k is {k}')
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                    print(f'  The outer j value is {j}')

                elif total > 0:
                    k -= 1
                    print(f'  The outer k value is {k}')

                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    print(ans)

                    j += 1
                    k -= 1
                    print(j , k)
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                        print(f'   The inner value of left is {j}')

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                        print(f'   The inner value of right is {k}')

        return ans


a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))

