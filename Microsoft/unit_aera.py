class Solution:
    #Function to find unit area of the largest region of 1s.
    def findMaxArea(self, grid):
        #Code here
        
               
        def dfs(i,j,grid):
    
            if i >=0 and j >=0 and i < len(grid) and j <len(grid[i]) and grid[i][j] == 1:
                # return 0

                grid[i][j] = 0
    
                up = dfs(i,j+1,grid)
                down = dfs(i,j-1,grid)
                left = dfs(i-1,j,grid)
                right = dfs(i+1,j,grid)
                first=dfs(i-1,j-1,grid)
                second=dfs(i-1,j+1,grid)
                third=dfs(i+1,j+1,grid)
                fourth=dfs(i+1,j-1,grid)
    
                return up + down + left + right + 1+first+second+third+fourth
            return 0


#             [[0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0], 
#              [0, 0, 0, 0, 0, 0, 0, -1, 1, 1, 0, 0, 0], 
#              [0, -1, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0], 
#              [0, -1, 0, 0, -1, -1, 0, 0, 1, 0, 1, 0, 0], 
#              [0, -1, 0, 0, -1, -1, 0, 0, 1, 1, 1, 0, 0], 
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
#              [0, 0, 0, 0, 0, 0, 0, -1, 1, 1, 0, 0, 0], 
#              [0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0]]

            
            
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    count = max(dfs(i,j,grid), count)
                    
        return count

T=1
for i in range(T):
    grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    obj = Solution()
    ans = obj.findMaxArea(grid)
    print(ans)

# } Driver Code Ends