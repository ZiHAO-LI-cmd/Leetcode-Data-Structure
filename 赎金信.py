class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)
        # 交集
        if (counter1 & counter2) == counter1:
            return True
        return False
