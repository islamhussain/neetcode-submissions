class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        nc = Counter(nums)
        nfs = nc.values()
        
        top_n = list(sorted(nfs, reverse=True))[:k]
        o = []
        for k,v in nc.items():
            if v in top_n:
                o.append(k)
        return o
        # return []