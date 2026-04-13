class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest_substring_length = 0
        substring = ''

        for c in s:
            if c in substring:
                largest_substring_length = max(largest_substring_length, len(substring))
                substring = substring[substring.find(c)+1:]
            substring = substring + c

        return max(largest_substring_length, len(substring))
        

if __name__ == '__main__':
    solution = Solution()

    print(solution.lengthOfLongestSubstring('abcabcbb'))  # 3
    print(solution.lengthOfLongestSubstring('bbbbb'))     # 1
    print(solution.lengthOfLongestSubstring('pwwkew'))    # 3