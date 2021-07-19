class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            s_ = ''.join(sorted(s))
            if s_ not in d:
                d[s_] = list()
            d[s_].append(s)
        return [d[k] for k in d]
