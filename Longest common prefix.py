class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s0 = strs[0]
        for i in range(len(s0)):
            ch = s0[i]
            for s in strs:
                if i >= len(s) or ch != s[i]:
                    return s[:i]
        
        return s0
       
