class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        maxL=height[l]
        maxR=height[r]
        res =0
        minh = min(maxL,maxR)
        while l<r:
            if maxL<maxR:
                l+=1
                maxL = max(maxL,height[l])
                minh = min(maxL,maxR)
                if minh>height[l]:
                    res+=minh-height[l]
            else:
                r-=1
                maxR = max(maxR,height[r])
                minh = min(maxL,maxR)
                if minh>height[r]:
                    res+=minh-height[r]
        return res
