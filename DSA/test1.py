
from collections import defaultdict 
  
# Function to find number of subarrays   
# with sum exactly equal to k.  
def findSubarraySum(arr, n, Sum):  
   
    # Dictionary to store number of subarrays  
    # starting from index zero having   
    # particular value of sum.  
    prevSum = defaultdict(lambda : 0) 
    
    res = 0 
    
    # Sum of elements so far.  
    currsum = 0 
    
    for i in range(0, n):   
    
        # Add current element to sum so far.  
        currsum += arr[i]  
    
        # If currsum is equal to desired sum,  
        # then a new subarray is found. So  
        # increase count of subarrays.  
        if currsum == Sum:   
            res += 1         
    
        # currsum exceeds given sum by currsum  - sum. 
        # Find number of subarrays having   
        # this sum and exclude those subarrays  
        # from currsum by increasing count by   
        # same amount.  
        if (currsum - Sum) in prevSum: 
            res += prevSum[currsum - Sum]  
            
    
        # Add currsum value to count of   
        # different values of sum.  
        prevSum[currsum] += 1 
       
    return res 

# Python3 program to find the number of  
# subarrays with sum exactly equal to k.  
from collections import defaultdict 
  
# Function to find number of subarrays   
# with sum exactly equal to k.  
def findSubarraySum(arr, n, Sum):  
   
    # Dictionary to store number of subarrays  
    # starting from index zero having   
    # particular value of sum.  
    prevSum = defaultdict(lambda : 0) 
    
    res = 0 
    
    # Sum of elements so far.  
    currsum = 0 
    
    for i in range(0, n):   
    
        # Add current element to sum so far.  
        currsum += arr[i]  
    
        # If currsum is equal to desired sum,  
        # then a new subarray is found. So  
        # increase count of subarrays.  
        if currsum == Sum:   
            res += 1         
    
        # currsum exceeds given sum by currsum  - sum. 
        # Find number of subarrays having   
        # this sum and exclude those subarrays  
        # from currsum by increasing count by   
        # same amount.  
        if (currsum - Sum) in prevSum: 
            res += prevSum[currsum - Sum]  
            
    
        # Add currsum value to count of   
        # different values of sum.  
        prevSum[currsum] += 1 
       
    return res  
   
if __name__ == "__main__": 
  
    arr =  [1,4,12,9]   
    Sum = 13
    n = len(arr)  
    print(findSubarraySum(arr, n, Sum))
    # arr =  [10, 2, -2, -20, 10]   
    # Sum = -10 
    # n = len(arr)  
    # print(findSubarraySum(arr, n, Sum))