class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        maxpile=piles[0]
        excess_h = h - n+1
        for i in range(n):
            maxpile = max(maxpile,piles[i])
        if excess_h == 1:
            return maxpile
        left = math.ceil(maxpile/excess_h)
        right = maxpile
        k=0
        while left<right:
            k = (left + right)//2
            curh = h
            for i in range(n):
                curh-= math.ceil(piles[i]/k)
            if curh<0:
                left = k+1
            else:
                right = k-1
        flag = 0
        while True:
            curh = h
            for i in range(n):
                curh-= math.ceil(piles[i]/k)
            if curh<0:
                k+=1
                if flag == 1:
                    break
                flag =1
            else:
                if k==1:
                    return k
                k-=1
        return k
