from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        s1 = strs[0]
        is_match = True

        for ci in range(len(s1)):
            if not is_match:
                break
            s1char = s1[ci]
            for i in range(1, len(strs)):
                if len(strs[i]) > ci and strs[i][ci] == s1char:
                    continue
                else:
                    is_match = False
            if is_match:
                prefix += s1char
        return prefix


# Cleaner alternative using zip(*strs) — stops at shortest string automatically,
# eliminating the manual bounds check.
#
# def longestCommonPrefix(self, strs: List[str]) -> str:
#     prefix = ""
#     for chars in zip(*strs):
#         if len(set(chars)) == 1:
#             prefix += chars[0]
#         else:
#             break
#     return prefix
