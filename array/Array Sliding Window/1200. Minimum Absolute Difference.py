class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:

        #step 1 : Sort the array
        arr.sort()
        print(arr)

        # find the minimum absolute diff
        min_diff = float('inf')

        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])

        # add the elements that have min_diff to res
        res = []
        for m in range(1,len(arr)):
            if arr[m] - arr[m-1] == min_diff:
                res.append([arr[m],arr[m-1]])
        
        return res



a = Solution()
print(a.minimumAbsDifference([4,2,1,3]))


