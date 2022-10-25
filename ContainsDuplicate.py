class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for n in nums:
            if n in d:
                return True
            else:
                d.add(n)
        return False
