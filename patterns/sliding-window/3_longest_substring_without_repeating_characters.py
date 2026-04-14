class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        substring = {}
        l = 0

        for r in range(len(s)):
            # expand: add s[r] to window
            substring[s[r]] = substring.get(s[r], 0) + 1

            # shrink: window invalid when any char appears more than once
            while max(substring.values()) > 1:
                substring[s[l]] -= 1
                if substring[s[l]] == 0:
                    del substring[s[l]]
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length
