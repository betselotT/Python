class Solution:
    def interpret(self, command: str) -> str:
        arr = []
        for i in range(len(command)):
            if command[i] == "(" and command[i+1] == ")":
                arr.append("o")
            if command[i] != "(" or command[i] != ")":
                arr.append(command[i])
        finalArr = [x for x in arr if x != "(" and x != ")"]
        return "".join(finalArr)