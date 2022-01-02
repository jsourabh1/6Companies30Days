from collections import defaultdict
def Anagrams(words,n):
  
    
    dict_1=defaultdict(list)
    for i in words:
        
        dict_1["".join(sorted(i))].append(i)
   
    
    
    return dict_1.values()
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ans=Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends