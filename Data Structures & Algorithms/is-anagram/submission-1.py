class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_1 = {}
        seen_2 = {}
        for char in s:
            if char in seen_1:
                seen_1[char] += 1
            else:
                seen_1[char] = 1

        for char in t:
            if char in seen_2:
                seen_2[char] += 1
            else:
                seen_2[char] = 1

        return seen_1 == seen_2