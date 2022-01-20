from typing import List
import re
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        
        list1=list(map(str,version1.split(".")))
        list2=list(map(str,version2.split(".")))
        # print(list1)
        if len(list1)<len(list2):
            
            for i in range(len(list2)-len(list1)):
                list1.append("0")
            
        elif len(list1)>len(list2):
            
            for i in range(len(list1)-len(list2)):
                list2.append("0")
        # print(list1,list2)
                
        for i in range(len(list1)):
          
                
            first=int(re.sub(r'0+(.+)', r'\1', list1[i]))

            second=int(re.sub(r'0+(.+)', r'\1', list2[i]))
            # print(first,second)
            if first<second:
                return -1
            if second<first:
                return 1
            
        return 0
                
                
                

        