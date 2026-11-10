class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        words=list(strs)


        for word in words:
            key="".join(sorted(word))

            if key not in groups:
                groups[key]=[]

            groups[key].append(word)
        return list(groups.values())
        