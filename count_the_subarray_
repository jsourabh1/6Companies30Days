
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        i=j=0
        product=1
        count=0
        while i<n:
            product*=a[i]
            while j<i and product>=k:
                product//=a[j]
                j+=1
                
            if product<k:
                count+=(i-j)+1
                
            i+=1
            
        return count
                
    
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends