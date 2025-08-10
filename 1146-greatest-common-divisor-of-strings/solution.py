class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2))-1, -1, -1):
            if len(str1) % (i+1) != 0 and len(str2) % (i+1) != 0:
                continue

            part = str1[0:i+1]

            if str1 == part * (len(str1)//(i+1)) and str2 == part * (len(str2)//(i+1)):
                return part
        
        return ""

