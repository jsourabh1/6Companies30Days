
class Solution:

    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        # code here

        row = col = 0
        rowend = r-1
        colend = c-1
        ans = []
        while row <= rowend and col <= colend:
            # print(row,col,colend,rowend)
            for i in range(col, colend+1):
                ans.append(matrix[row][i])

            row += 1

            for i in range(row, rowend+1):
                ans.append(matrix[i][colend])

            colend -= 1

            if row <= rowend:
                for i in range(colend, col-1, -1):
                    ans.append(matrix[rowend][i])

            rowend -= 1
            if col <= colend:
                for i in range(rowend, row-1, -1):
                    ans.append(matrix[i][col])

            col += 1

        return ans
#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends
