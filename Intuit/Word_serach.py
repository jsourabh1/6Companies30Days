        
class Solution:
	def isWordExist(self, board, word):
		#Code here
		 
        
        def helper(grid,row,col,string):
            
            if not string:
                return True
                
          #  [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
            for i,j in [[-1,0],[0,1],[1,0],[0,-1]]:
                
                xi,yj=row+i,col+j
                
                if xi>=0 and xi<len(grid) and yj>=0 and yj<len(grid[0]) and grid[xi][yj]==string[0]:
                   temp=grid[xi][yj]
                   grid[xi][yj]=-1
                  # print(string,temp)
                   if  helper(grid,xi,yj,string[1:]):
                       return True
                  # print(string)
                   
                   grid[xi][yj]=temp
                       
            return False
            
        for i in range(len(board)):
            
            for j in range(len(board[0])):
                
                if board[i][j]==word[0]:
                    temp=board[i][j]
                    board[i][j]=-1
                    
                    if helper(board,i,j,word[1:]):
                        return True
                    
                    board[i][j]=temp
                        
        return False
            
            

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n, m = map(int, input().split())
        board = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            board.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(board, word)
        if(ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends