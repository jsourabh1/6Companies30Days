from collections import defaultdict
class Solution:
    def FirstNonRepeating(self, s):
        # Code here
        
        dict_1=defaultdict(lambda:0)
        
        start=[]
        res=""
        
        for i in s:
            
            dict_1[i]+=1
            
            if dict_1[i]==1:
                start.append(i)
                
            while start and dict_1[start[0]]>1:
                start.pop(0)
                
            if not start:
                res+="#"
                
            else:
                res+=start[0]
                
        return res
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)

# } Driver Code Ends