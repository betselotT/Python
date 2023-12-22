class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        noRep = ''.join(OrderedDict.fromkeys(key))
        letters = list(string.ascii_lowercase)
        result = noRep.replace(" ", "")
        keyLetter = {}
        for i in range(0, 26):
            keyLetter[result[i]] = letters[i]

        finalResult = []
        for i in range(len(message)):
            if (message[i] == " "):
                finalResult.append(" ")
            else:
                finalResult.append(keyLetter[message[i]])
        return "".join(finalResult)