# Python Question 7: Find the Missing Number
# Given a list containing n distinct numbers from the range 0 to n, find the one missing number.

# Input:  [3, 0, 1]
# Output: 2

def find(arr):
    n = len(arr)
    original = 0
    for i in arr:
        original = original+i
    
    real = (n*(n+1))/2

    return real-original


# this takes O(n2), as inner if condition needs another n iterations to check.
def find(arr):
    
    for i in range(0,len(arr)+1):
        if i not in arr:
            return i
        

# what if integer overflow
# then we should use the XOR operator --> XOR cancels out matching pairs
# x ^ x = 0
# x ^ 0 = x

def find(arr):
    n = len(arr)
    missing =n

    for i in range(n):
        missing ^=i^arr[i]

    return missing

# for this ex.  [3,0,1]
# missing = 3
# range(n)  --> 0,1,2
# arr = 3,0,1

# now, 3 ^ (0^1^2) ^ (3^0^1)  ---> all same pairs cancels out and raming is 2.