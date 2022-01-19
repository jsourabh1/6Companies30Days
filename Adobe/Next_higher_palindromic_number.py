from collections import Counter


class Solution:
    def nextPalin(self, N):
        #code here
        arr = list(map(int, N.strip()))

        if len(arr) == 1:
            return -1

        n = len(arr)

        extra = -1

        if n % 2 != 0:

            extra = arr[n//2]

        #make a duplicate array

        temp = arr[:n//2]

        # Now we have to find the inversion point in the string :
        # Make a array to track the element
        temp2 = []
        flag = False

        for i in range(n//2-1, -1, -1):

            if temp2:
                temp2.sort()
                for j in range(len(temp2)):
                    if temp2[j][0] > temp[i]:
                        temp[i], temp[temp2[j][1]] = temp[temp2[j][1]], temp[i]
                        flag = True
                        break
                if flag:
                    break
            temp2.append([arr[i], i])
            # print(temp2)

        if not flag:
            return -1

        temp = temp[:i+1]+sorted(temp[i+1:])

        temp2 = temp[::]

        if extra != -1:
            temp.append(extra)

        temp.extend(temp2[::-1])

        return "".join(map(str, temp))


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.nextPalin(s))
# } Driver Code Ends
