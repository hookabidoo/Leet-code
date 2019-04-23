class Solution:
    def twoSum(self, nums,target):
        num = {nums[i]:i for i in range(len(nums))}
        # create a dict 
     
        print(num)
        for idx, val in enumerate(nums):
            complement = target - val
            print(complement)
            if complement in num:
                if num.get(complement) != idx:
                    return idx, num.get(complement)