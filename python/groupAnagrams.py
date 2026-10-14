# Python Question 8: Group Anagrams
# Given a list of strings, group together all strings that are anagrams of each other.

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

# Output: [["eat", "tea", "ate"],
#          ["tan", "nat"],
#          ["bat"]]



def group(arr):
    freq = {}

    for i in arr:
        temp = "".join(sorted(i))
        if temp not in freq:
            freq[temp] = []     # --> i have to initilise the arr as a value for the freq dict.

        freq[temp].append(i)

    ans = []

    for key, value in freq.items():
        ans.append(value)

    # or the easy method  return list(freq.values())

    return ans


# why list() used over freq.values() returns a view of all the values stored in the dictionary.

# dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
