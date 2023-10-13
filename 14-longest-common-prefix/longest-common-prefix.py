class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
# The above code took almost 60 ms to execute

# ##                      EASIER WAY     (tooks 77ms --longer time than above)     
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""  # If the input list is empty, return an empty string
        
#         prefix = ""
#         for i in range(len(strs[0])):
#             char = strs[0][i]  # Get the character from the first string
#             for s in strs:
#                 if i >= len(s) or s[i] != char:
#                     return prefix
#             prefix += char  # Add the character to the prefix
        
# #         return prefix  # Return the common prefix found so far

        