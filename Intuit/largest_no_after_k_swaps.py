class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        #code here
        ans=[]
        
        for i in range(len(s)):
            
            ans.append([i,int(s[i])])
            
        ans.sort(reverse=True,key=lambda x:(x[1],x[0]))
        temp=list(map(int,s.strip()))
        # print(ans)
        for i in range(len(s)):
            
            while ans and (ans[0][0]<i):
                ans.pop(0)
                
            if not ans:
                break
            if ans[0][1]==int(s[i]):
                continue
            # if [i,int(s[i])] not in ans:
            #     continue
            index=ans.index([i,int(s[i])])
            
            
            
            ans[0][0],ans[index][0]=ans[index][0],ans[0][0]
            
            temp[i],temp[ans[index][0]]=ans[0][1],temp[i]
            # print(temp,ans)
            k-=1
            if k==0:
                break
        # print(temp)  
        return "".join(map(str,temp))


obj=Solution()

obj.findMaximumNum("1234567",4)