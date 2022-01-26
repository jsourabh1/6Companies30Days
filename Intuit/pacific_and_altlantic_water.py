class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
   
        
        row=len(heights)
        col=len(heights[0])
        
        pacific=[[False]*(col) for i in range(row)]
        
        atlantic=[[False]*(col) for i in range(row)]
        
        def dfs(grid,row,col,value,temp):
            # print(row,col)
            
            if row<0 or row>len(grid)-1 or col<0 or col>len(grid[0])-1:
                return 
            
            if grid[row][col]<value or temp[row][col]:
                return 
            temp[row][col]=True
        
            for i,j in [[-1,0],[0,1],[1,0],[0,-1]]:
                
                dfs(grid,row+i,col+j,grid[row][col],temp)

        
        for i in range(col):
            
            dfs(heights,0,i,-float("inf"),pacific)
            dfs(heights,row-1,i,-float("inf"),atlantic)
            
        for i in range(row):
            
            dfs(heights,i,0,-float("inf"),pacific)
            dfs(heights,i,col-1,-float("inf"),atlantic)
            
        ans=[]
        
        for i in range(row):
            for j in range(col):
                
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])
        return ans
            
            
        
            
        