# function should return the missing number
# else return -1

def missingNumber(inp):
    # Code here
    
    
    def startswith(idx, num):
        # quick startswith function to avoid string slicing
        num = str(num)
        if len(num) > len(inp)-idx:return False
        i = 0
        while idx < len(inp) and i < len(num):
            if inp[idx] != num[i]:return False    
            i += 1
            idx += 1
        return True

    def isContinousSeq(startIndex, num):
        # check if we can make continous sequence fixing num as first number from the string[startIndex:]
        if startIndex >= len(inp): return True
        if len(str(num)) > len(inp)-startIndex: return False
        return isContinousSeq(startIndex+len(str(num)), num+1) if startswith(startIndex, num) else False

    def findFirstMismatch(idx, num):
        if startswith(idx, num):
            return findFirstMismatch(idx+len(str(num)), num+1)
        return idx, num
    for d in range(1, min(len(inp)+1, 7)):
        # we got to fix the first number
        # d representing digit
        first=int(inp[:d])
        # we need to check we could find first+1 or first+2 now
        firstMismatchIdx, miss=findFirstMismatch(0, first)
        if firstMismatchIdx >= len(inp):
            continue
        if isContinousSeq(firstMismatchIdx, miss+1):
            return miss
    return -1
            
            
            


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        string = input().strip()
        print(missingNumber(string))
# Contributed by: Harshit Sidhwa

# } Driver Code Ends