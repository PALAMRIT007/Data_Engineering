# Python Question 4: Merge Overlapping Intervals
# Given a list of intervals, merge all overlapping intervals and return the resulting list.

# Input:  [[1, 3], [2, 6], [8, 10], [9, 12]]

# Output: [[1, 6], [8, 12]]

# Time: \(O(n \log n)\) due to sorting.
# Extra space: \(O(n)\) for the output list.

def merge(arr):
    arr.sort()
    ans= []

    ans.append(arr[0])

    for i in range(1,len(arr)):
        temp = arr[i]
        last = ans[-1]
        if temp[0] <= last[1]:
            # merging
            last[1] = max(last[1],temp[1])    #durectly nahi daalna hai, max lema hai dono me se
        else:
            ans.append(arr[i])

    return ans

