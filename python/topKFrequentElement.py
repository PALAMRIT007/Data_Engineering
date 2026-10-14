# Python Question 11: Top K Frequent Elements
# Given a list of integers nums and an integer k, return the k most frequent elements.

# Input:  nums = [1, 1, 1, 2, 2, 3]
#         k = 2

# Output: [1, 2]

from collections import Counter
def topk(arr,k):
    ans=[]
    freq = Counter(arr)

    for key,val in freq.items():
        ans.append((val,key))

    ans.sort(reverse=True)

    final = []
    for i in range(k):
        final.append(ans[i][1])

    return final

# Complexity:
# - Time: \(O(n + m\log m)\)     m is unique element in arr
# - Space: \(O(m)\)

