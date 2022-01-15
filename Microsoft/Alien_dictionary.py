from collections import defaultdict
class Solution:
    def findOrder(self,words, n, k):
    # code here
    
        graph={c:set() for i in words for c in i}
        
        
        for i in range(len(words)-1):
            
            w1,w2=words[i],words[i+1]
            
            minlen=min(len(w1),len(w2))
            
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
                
            for j in range(minlen):
                
                if w1[j]!=w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
                    
        visited=set()
        visit=set()
        flag=True
        def dfs(node,visited,visit,ans):
            
            visited.add(node)
            visit.add(node)
            
            for i in graph[node]:
                
                if i not in visited:
                    dfs(i,visited,visit,ans)
                    
                if i in visit:
                    flag=False
                    return 
            ans.append(node)
            visit.remove(node)
            
        ans=[]
        for i in graph:
            
            if i not in visited:
                dfs(i,visited,visit,ans)
                
        if not flag:
            return ""
        return ans[::-1]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends