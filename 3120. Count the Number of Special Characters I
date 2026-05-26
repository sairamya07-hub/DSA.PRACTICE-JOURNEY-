class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        count = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in s and ch.upper() in s:
                count += 1

        return count
