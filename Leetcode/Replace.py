class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = address.replace('.', '[.]')
        return answer