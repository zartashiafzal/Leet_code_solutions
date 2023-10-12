class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Count the characters of the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1  #to decrement the counter in this case 
            #otherwise it will be infinite loop

        return length

# time complexity==> O(n)
# Space complexity ==> O(1)
