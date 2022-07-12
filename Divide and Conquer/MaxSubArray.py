#Divide and conquer approach for max subaary problem

def maxCrossingsum(arr, l, m ,h):
    #Left Elements
    sm = 0
    left_sum = -1000
    for i in range(m,l-1,-1):
        sm = sm+arr[i]

        if(sm>left_sum):
            left_sum = sm
    #Right Elements
    sm = 0
    right_sum = -1000
    for i in range(m+1,h+1):
        sm = sm + arr[i]
        if(sm > right_sum):
            right_sum = sm

    return max(left_sum + right_sum, left_sum,right_sum)

def maxSubArraySum(arr,l,h):
    #base case only 1 element
    if(l==h):
        return arr[l]
    mid = (l+h)//2
    return max(maxSubArraySum(arr,l,mid),maxSubArraySum(arr,mid+1,h),maxCrossingsum(arr,l,mid,h))

arr= [-1,-5,6,-2,-3,1,5,-6]
print(maxSubArraySum(arr,0,len(arr) - 1))
