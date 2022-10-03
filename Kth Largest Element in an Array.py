class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxn = nums[0]
        minn = nums[0]
        for i in nums:
            maxn = max(maxn,i)
            minn = min(minn,i)
        
        d = {}
        for i in range(minn,maxn+1):
            d[i] = 0
        
        for i in nums:
            d[i]+=1
        n=0
        while 1:
            n+=d[maxn]
            if n>=k:
                return maxn
            maxn-=1
