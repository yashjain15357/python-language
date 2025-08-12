class Solution:
    def subArraySum(self,arr, n, s):
        for i in range(0,n+1) :
            a = 0
            for j in range(i,n+1):
                a = arr[j]+a
                if a==s:
                    print(j+1)
                    break
                
                    

arr=[1,2,3,4,5]
n= len(arr)
s=9
obj = Solution()
result= obj.subArraySum(arr,n,s)
print(result)