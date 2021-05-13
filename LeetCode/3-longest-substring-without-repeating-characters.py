class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return len(s)
        hashMap = dict()
        max_len = 0
        begin_index = 0

        for i, si in enumerate(s):
            if si in hashMap.keys():
                new_begin_index = hashMap[si] + 1
                begin_index = begin_index if begin_index > new_begin_index else new_begin_index
            hashMap[si] = i

            windows_len = i - begin_index
            max_len = windows_len if windows_len > max_len else max_len

        return max_len + 1


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"), 3)
print(s.lengthOfLongestSubstring("bbbbb"), 1)
print(s.lengthOfLongestSubstring("pwwkew"), 3)
print(s.lengthOfLongestSubstring(""), 0)
print(s.lengthOfLongestSubstring(" "), 1)
print(s.lengthOfLongestSubstring("abba"), 2)
print(s.lengthOfLongestSubstring("dvdf"), 3)
