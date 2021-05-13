class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        window_len = 10
        hashSet = set()
        res = list()
        for i in range(0, len(s) - window_len + 1):
            print(s[i:i + window_len])
            if s[i:i + window_len] not in hashSet:
                hashSet.add(s[i:i + window_len])
            else:
                res.append(s[i:i + window_len])
        return res