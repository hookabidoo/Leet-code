class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        diff_dict = {}
        idx = 1
        
        
        for num in A:
            if num not in diff_dict:
                diff_dict[num] = 1
            else: 
                diff_dict[num] = idx+1
            
        for i in A:
            if diff_dict[i] > 1:
                return i
        # print(diff_dict) 
       
# very smart solution by finding the first dubplicate 
# from collections import defaultdict

# class Solution:
#     def repeatedNTimes(self, A: List[int]) -> int:
#         d = set()
#         for a in A:
#             if a not in d:
#                 d.add(a)
#             else: return a