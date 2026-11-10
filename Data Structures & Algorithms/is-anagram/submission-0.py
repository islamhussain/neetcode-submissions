class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        sa = Counter(s)
        ta = Counter(t)
        if sa.keys() != ta.keys():
            return False
        for i in sa.keys():
            if sa[i] != ta[i]:
                return False
        return True
        
        