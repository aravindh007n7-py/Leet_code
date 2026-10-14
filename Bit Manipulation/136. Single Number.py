class Solution:
    def singleNumber(self , nums:list[int])-> int:
        # num_set = set()
        # for i in nums:
        #     if i not in num_set:
        #         num_set.add(i)
        #     else:
        #         num_set.remove(i)
        # return list(num_set)[0]
        # /Time complexity - O(n)
        # /Space complexity - O(n)



        # using hashing number frequency if duplicate num appear set the num freq to 1 else num freq to 0
        # hash = {}
        # for num in nums:
        #     if num not in hash:
        #         hash[num] = 0
        #     else:
        #         hash[num] = 1

        # for val in hash:
        #     if hash[val] == 0:
        #         return val
        # Time complexity - O(n)
        # Space Complexity - O(n)




            
        # using bit manipulation
        #  0 ^ single_num == single_num
        #  single_num ^ single_num == 0      
        xor = 0
        for num in nums:
            print('num',num)
            xor ^= num
            print(xor)
        return xor
        # /Time complexity O(n)- for iterate through the array
        # /Space complexity O(1) - for xor variable store single int only


a = Solution()
print(a.singleNumber(nums= [4,2,1,2,1])) 

print(5^6)