#from collections import defaultdict
class Solution:
     def groupAnagrams(self, strs: List[str]) -> List[List[ str ]]:
        res = defaultdict(list) 
# Create a dictionary to store anagrams or 
#we can say mapping charCount to list of Anagrams

        for s in strs:
            count= [0]* 26 # Initialize a list to count characters (a to z)
            for c in s:
                count[ord(c)-ord("a")] += 1   # Count characters using ASCII values

# We cannot take list as a key in python so we convert the list to a tuple and use it as a key in the dictionary
            res[tuple(count)].append(s)  # Group anagrams based on character count          
        return res.values()  # Convert values (anagram groups) of the dict to a list &return
         
# Time Complexity ==> O(m.n)


# # --------- Another solution by sorting but complexity is more  -------------

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = {}

#         for word in strs:
#             sorted_word = ''.join(sorted(word))  # Sort the characters of the word
#             if sorted_word in anagrams:
#                 anagrams[sorted_word].append(word)  # Add the word to the existing anagram #group
#             else:
#                 # anagrams[sorted_word] = [word]  # Create a new anagram group with the sorted #word

#         return list(anagrams.values())  # Convert values (anagram groups) of the dictionary to #a list and return

        