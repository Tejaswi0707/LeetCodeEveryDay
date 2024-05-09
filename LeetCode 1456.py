class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        l = count = res = 0
        for r, c in enumerate(s):
            count += 1 if c in vowels else 0
            if (r - l) + 1 == k:
                res = max(res, count)
                count -= 1 if s[l] in vowels else 0
                l += 1
        return res
