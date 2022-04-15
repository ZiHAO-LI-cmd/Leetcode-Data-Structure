class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        counter = Counter(s)
        for key, value in counter.items():
            if value == 1:
                return s.find(key)
        return -1