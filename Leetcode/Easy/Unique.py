class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        wordMap = {
            "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
            "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
            "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
            "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
            "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
            "z": "--..",
        }

        newArr = set()
        for i in words:
            morse = ""
            for j in i:
                morse += wordMap[j]
            newArr.add(morse)
        print(newArr)
        return len(newArr)
