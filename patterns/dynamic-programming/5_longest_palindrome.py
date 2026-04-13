class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        # Iterate through string w/ 2 pointers 
        # first forwards, second backwards, stop at largest palendrom, 
        # Stop traversing if len of return_val is longer than the difference between pointers

        def is_palendrome(sub_string, longest_palindrome):
            if sub_string == sub_string[::-1]:
                if len(sub_string) > len(longest_palindrome):
                    longest_palindrome = sub_string
                    return True
            return False

        for p1 in range(len(s)):
            for p2 in range(len(s),-1,-1):
                if p2 - p1 > len(longest_palindrome) and p2 >= p1:
                    sub_string = s[p1:p2]
                    if is_palendrome(sub_string, longest_palindrome):
                        longest_palindrome = sub_string
        

        return longest_palindrome
            
        
if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome(s))