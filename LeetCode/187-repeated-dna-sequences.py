class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        window_len = 10
        hashSet = set()
        res = set()
        for i in range(0, len(s) - window_len + 1):
            if s[i:i + window_len] not in hashSet:
                hashSet.add(s[i:i + window_len])
            else:
                res.add(s[i:i + window_len])
        return list(res)
