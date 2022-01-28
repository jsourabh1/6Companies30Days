from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        
        graph=defaultdict(list)
        index=0
        for i,j in edges:
            
            graph[i].append([j,index])
            graph[j].append([i,index])
            index+=1
            
        
        

        queue=[]
        queue.append(start)
       
        prob=[0.0]*(n)
        prob[start]=1.0

        while queue:


            node=queue.pop(0)

            for i ,pro in graph[node]:

                if prob[node]*succProb[pro]>prob[i]:
                    prob[i] = prob[node] * succProb[pro]
                    
                    queue.append(i)
        
        
        return prob[end]



      
                
        