# Python Question 6: Flatten a Nested List
# Given a list that can contain integers or other nested lists, flatten it into a single list.


# Input:  [1, [2, [3, 4]], 5]
# Output: [1, 2, 3, 4, 5]

# Time: \(O(n)\), where \(n\) is the total number of elements.
# Space: \(O(n)\) for the stack and output list.

def unpack(top, s):
    for i in range(len(top)-1,-1,-1):
        s.append(top[i])



def flatten(arr):
    ans=[]
    s = []  # trear it as a stack
    # reverse arr daal diya s me
    for i in range(len(arr)-1,-1,-1):
        s.append(arr[i])

    while(len(s) !=0):
        top = s.pop()   #it will remove the last elemnt and return it, i stack language, its top.
        if isinstance(top,int):
            ans.append(top)
        else:
            unpack(top,s)

    return ans


    
