class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        ds = {}
        for i in range(len(strs)):
            ci = frozenset(Counter(strs[i]).items())
            if not ds.get(ci):
                ds[ci] = [i]
            else:
                ds[ci].append(i)
        grps = []
        for il in ds.values():
            grpi = []
            for i in il:
                grpi.append(strs[i])
            grps.append(grpi)
        return grps
                


            
        