class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      

        if len(set(nums))==len(nums):
            return False
        else:
            dict1 = {}
            for index, val in enumerate(nums):
                if val not in dict1.keys():
                    dict1[val]=index
                    # print(dict1)
                    
                elif val in dict1.keys() and (index - dict1[val] <= k):
                    # print('2')
                    # print(dict1)
                    # print(dict1[val])
                    
                    return True 
                    
                else:
                    dict1[val]=index
                
            return False 