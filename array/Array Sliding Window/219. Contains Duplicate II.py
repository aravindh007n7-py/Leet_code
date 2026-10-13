class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()
        for i , v in enumerate(nums):
            if v in seen:
                return True
            else:
                seen.add(v)

            # to maintain the size of sliding window k- size
            if len(seen) > k:
                seen.remove(nums[i- k])
        return False

Duplicate2 = Solution()
print(Duplicate2.containsNearbyDuplicate([1,0,1,1] , k = 1))

            
