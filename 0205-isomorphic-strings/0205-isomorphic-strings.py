class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # ISOMPORPHIC STRING 

        mapping_st = {}
        mapping_ts = {}
        for i in range (len(s)):
            if s[i] in mapping_st:
                if mapping_st[s[i]] != t[i]:
                    return False
            else:
                mapping_st[s[i]] = t[i]
            if t[i] in mapping_ts:
                if mapping_ts[t[i]] != s[i]:
                    return False 
            else :
                mapping_ts[t[i]] = s[i]
        return True 
        