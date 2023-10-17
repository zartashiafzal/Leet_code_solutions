class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1   # Initializing left & right pointers
        while l < r:           # While left pointer is less than right pointer
            while l < r and not self.alphanum(s[l]): 
                l += 1         # Increment right pointer, if not alphanumeric
            while l < r and not self.alphanum(s[r]):
                r -= 1         # Decrement right pointer, if not alphanumeric
# If alphanumeric then compare below after making sure each characteris a #lower case and left and right characters are not equal then return false
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1              # Update left pointer, increment to right
            r -= 1              # Update right pointer, decrement to left
        return True             # If paindrome return TRUE

    # Create own alpha-numeric function to check if each character passing #from above code is alphanumeic or not (before actually doing the comparison)
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
