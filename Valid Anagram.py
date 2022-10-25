class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for a in s:
            if a in d.keys():
                d[a]+=1
            else:
                d[a]=1
        for a in t:
            if a not in d.keys() or d[a] == 0:
                return False
            else:
                d[a]-=1
        for i in d.keys():
            if d[i] !=0:
                return False
        return True
