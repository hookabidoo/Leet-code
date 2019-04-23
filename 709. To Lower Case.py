
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()



# fastest way is working with ascii 


# class Solution:
#     def toLowerCase(self, str: 'str') -> 'str':
#         lower = ""
        
#         for s in str:
#             # Convert s to lowercase if it's upper
#             if s >= "A" and s <= "Z":
#                 lower += chr(ord(s) - ord('A') + ord('a'))
#             else:
#                 lower += s
        
#         return lower