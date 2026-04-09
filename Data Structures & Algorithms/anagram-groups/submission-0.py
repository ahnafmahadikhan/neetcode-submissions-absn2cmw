from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for sp in strs:
            key =''.join(sorted(sp))
            res[key].append(sp)
        return list(res.values())