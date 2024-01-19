class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        right = 0
        while right < len(word):
            if word[right] != ch:
                right += 1
            elif word[right] == ch:
                word_list = list(word)
                while left < right:
                    word_list[left], word_list[right] = word_list[right], word_list[left]
                    left += 1
                    right -= 1
                return "".join(word_list)
        return word