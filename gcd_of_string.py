import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1+str2 != str2+str1:
            return ""
        ans = ""

        for i in range(min(len(str2), len(str1))):

            if str1[i] == str2[i]:
                ans += str1[i]

        if not ans:
            return ans

        temp = math.gcd(len(str1), len(str2))

        return ans[:temp]
