class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        max_window = 0
        l = 0

        for r in range(len(s)):
            # expand: add s[r] to window
            window[s[r]] = window.get(s[r], 0) + 1

            # shrink: replacements needed = window_size - max_frequency
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            max_window = max(max_window, r - l + 1)

        return max_window
