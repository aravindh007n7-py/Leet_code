class Solution:
    def maxProfit(self, prices:list[int])->int:
        l, r = 0, 1
        maxp = 0
        while r!= len(prices):
            if prices[l] < prices[r]:
                prof = prices[r]-prices[l]
                maxp = max(maxp,prof)
                print(f'Profit{maxp}')
            else:
                l = r
            r+= 1
        return maxp
    
a = Solution()
print(a.maxProfit([3,2,8,9]))