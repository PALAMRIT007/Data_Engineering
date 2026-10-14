# Python Question 2: Remove Duplicates While Preserving Order
# Given a list of integers, remove duplicates while preserving the original order of elemen

# Input:  [3, 1, 3, 2, 1, 4]
# Output: [3, 1, 2, 4]


def remove(arr):
    i=0
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0)+1
    
    return freq.keys()

# other ways is just store if not present

def remove(arr):
    i=0
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
    
    return freq.keys()


# without using the extra space but O(n2)

def remove(arr):
    i=0
    while(i<len(arr)):
        j = i+1
        while(j<len(arr)):
            if arr[i] == arr[j]:
                arr.pop(j)
            else:
                j +=1

        i+=1

    return arr
