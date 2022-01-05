#TLE solution
# import sys
start="a"
dict_1={}
for i in range(27):
    dict_1[i+1]=chr(ord(start)+i)
print(dict_1)
# class Solution:
#     def CountWays(self, str):
#         # Code here

#         def helper(ans, string, index):
#             nonlocal str
#             print(string, index, ans)

#             if index == len(str):

#                 listt = list(string.split(":"))
#                 temp = ""
#                 print(listt)
#                 # for i in listt[1:]:

#                 #     if int(i) > 27:
#                 #         return

#                 #     temp += ord(int(i))
#                 # ans.append(temp)
#                 return

#             helper(ans, string+":"+str[index], index+1)

#             if index < len(str)-1:
#                 helper(ans, string+":"+str[index]+str[index+1], index+2)
#         ans = []
#         helper(ans, "", 0)
#         return len(ans)
# obj=Solution()
# obj.CountWays("123")


# #{
# #  Driver Code Starts
# #Initial Template for Python 3
# # sys.setrecursionlimit(10**6)
# # if __name__ == '__main__':
# #     T = int(input())
# #     for i in range(T):
# #         str = input()
# #         ob = Solution()
# #         ans = ob.CountWays(str)
# #         print(ans)

# # } Driver Code Ends



import sys


class Solution:
    def CountWays(self, s):

        def decode(s, i=0, cache={}):
            if i in cache:
                return cache[i]
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            count = decode(s, i+1)
            if (i+1 < len(s)) and (int(s[i:i+2]) <= 26):
                count += decode(s, i+2)
            if i not in cache:
                cache[i] = count
            return cache[i]

        return (decode(s) % ((10**9)+7))


#{
#  Driver Code Starts
#Initial Template for Python 3
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.CountWays(str)
        print(ans)

# } Driver Code Ends
