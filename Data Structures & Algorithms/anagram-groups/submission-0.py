class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_groups = {}

        for i, word in enumerate(strs):
            master_key = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}

            for char in word:
                master_key[char] += 1
            
            key = tuple(master_key.values())

            if key in seen_groups:
                seen_groups[key].append(word)
            else:
                seen_groups[key] = [word]
            
        return(list(seen_groups.values()))