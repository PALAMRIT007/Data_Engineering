# a= [1,1,2,2,3,3,3,4,4,5] 
# - move duplicates values in the end in order
# Output : [1, 2, 3, 4, 5, 1, 2, 3, 3, 4].


from collections import Counter

# this i wrote in interview(ganit)
def move(arr):
    freq= Counter(arr)

    final = list(freq.keys())       [1,2,3,4,5] [1,2,3,3,4]

    # for k,v in freq.items():
    #     v = v-1


    for k,v in freq.items():
        for i in range(v-1):
            final.append(k)

    return final

# if preserving order and maing it work on all. -- optimised approach

def move(arr):
    seen = []
    dup =[]
    seen_set = set()

    for i in arr:
        if i in seen_set:
            dup.append(i)
        else:
            seen_set.add(i)
            seen.append(i)

    return seen + dup


			
			
	