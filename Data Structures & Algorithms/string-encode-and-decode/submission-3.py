class Solution:

    def encode(self, strs: List[str]) -> str:
        if "" in strs:
            for i in range(len(strs)):
                if strs[i] ==  "":
                    print("empty")
                    strs[i] = "__empty__"
        print("__$$__".join(strs))
        return "__$$__".join(strs)

    def decode(self, s: str) -> List[str]:
        if not '__empty__' in s:
            if not s:
                return []
            return s.split("__$$__")
        
        strs = s.split("__$$__")

        for i in range(len(strs)):
            if strs[i] == "__empty__":
                strs[i] = ""
        return strs