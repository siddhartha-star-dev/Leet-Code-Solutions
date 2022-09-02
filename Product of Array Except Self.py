class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(len(nums)-1):
            ans.append(nums[i]*ans[i])
        
        postfix= 1
        
        for i in range(len(nums)-2,-1,-1):
            postfix *= nums[i+1]
            ans[i] *= postfix
        
        return ans
