# Python Question 3: Two Sum
# Given a list of integers nums and an integer target, return the indices of two 
# numbers whose sum equals the target.

# Input: arr = [2, 7, 11, 15]
#        target = 9

# Output: [0, 1]

def twosum(arr,t):
    freq = {}
    for idx,i in enumerate(arr):
        comp = t-i
        if comp in freq:
            return [idx,freq[comp]]
        
        
        freq[i] = idx

    return None