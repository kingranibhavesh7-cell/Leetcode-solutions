class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        ref = strs[0]
        for i in range (len(ref)):
            ch = ref[i]
            for word in strs:
                if i >= len(word) or word[i] != ch :
                    return result
            result += ch
        return result  
        