class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0

        for char in s:
            if char == '(':
                leftMin += 1
                leftMax += 1
            elif char == ')':
                leftMin = max(leftMin - 1, 0)
                leftMax -= 1
                if leftMax < 0:
                    return False
            elif char == '*':
                leftMin = max(leftMin - 1, 0)
                leftMax += 1

        return leftMin == 0