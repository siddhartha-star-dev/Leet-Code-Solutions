class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1 = 0
        rob2 = 0
        last = nums.pop()
        for n in nums:
            temp = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = temp
        m1 = rob2
        del nums[0]
        nums.append(last)
        rob1 = 0
        rob2 = 0
        for n in nums:
            temp = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = temp
        return max(m1,rob2)
