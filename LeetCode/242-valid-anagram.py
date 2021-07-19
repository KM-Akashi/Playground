class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for si in s:
            if si not in d:
                d[si] = 0
            d[si] += 1

        for ti in t:
            if ti not in d:
                return False
            else:
                d[ti] -= 1

        for k in d:
            if d[k] != 0:
                return False

        return True