class Solution(object):
    def twoSum(self, nums, target):
        diction = {}
        ans_list = []
        for i in range(len(nums)):
            if nums[i] in diction:
                if target/2 != nums[i]:
                    del diction[nums[i]]
                else:
                    ans_list.append(i)
                    ans_list.append(diction[nums[i]])
            else:
                diction[nums[i]] = i
        for i in diction:
            comp = target-i
            if comp in diction and comp!=i and diction[comp] not in ans_list:
                ans_list.append(diction[comp])
                ans_list.append(diction[i])
        return ans_list
