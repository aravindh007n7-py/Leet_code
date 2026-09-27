# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and 
# nums[j] < nums[i].

# Return the answer in an array.

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        hash = {i:v for i, v in enumerate(nums)}
        original_keys = set(hash.keys())
        output = []
        for num in range(0,len(nums)):
            print(num)
            comparing_keys = original_keys - set().union([num])
            min_val = [''+'1' for y in list(comparing_keys) if hash[num] > hash[y]]
            output.append(len(min_val))
        return output

a = Solution()
print(a.smallerNumbersThanCurrent([8,1,2,2,3]))