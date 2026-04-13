# 8. String to Integer (atoi)
"""
currently facing issues with one off erros like "+". Need to look into most efficient way to do this.

"""

class Solution:
    def myAtoi(self, s: str) -> int:
        
        def step_1_processing(s):
            for i in range(len(s)):
                if s[i] != " ":
                    s = s[i:]
                    return s
        
        def step_2_processing(s):
            if s[0] in ["+", "-"]:
                return s[0], s[1:]
            else:
                return "+", s
        
        def step_3_processing(s):
            if not s:
                return ""
            first_index = None
            last_index = None
            for i in range(len(s)):
                last_index = i
                if s[i] == "0":
                    continue
                elif s[i] in ["1","2","3","4","5","6","7","8","9"]:
                    if first_index is None:
                        first_index = i
                    continue
                else:
                    if first_index is None:
                        return "0"
                    else:
                        last_index -= 1
                    break
            return s[first_index:last_index+1]
        if not s:
            return 0
        s = step_1_processing(s)
        pos_or_neg, s = step_2_processing(s)
        s = step_3_processing(s)
        s = pos_or_neg + s
        val = int(s)
        if val < -2**31:
            return -2**31
        if val > 2**31 - 1:
            return 2**31 - 1
        return int(s)
    
            

    
if __name__ == "__main__":
    print(Solution().myAtoi("   -42"))
    print(Solution().myAtoi("   +"))

