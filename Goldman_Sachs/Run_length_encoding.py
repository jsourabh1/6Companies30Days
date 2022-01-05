#Function should return complete string
def encode(arr):
    # Code here
    
    count=1
    ans=""
    for i in range(1,len(arr)):
        
        if arr[i-1]!=arr[i]:
            
            ans+=arr[i-1]+str(count)
            count=1
            
        else:
            count+=1
            
    ans+=arr[-1]+str(count)
    
    return ans
        
        

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends