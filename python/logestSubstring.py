# Python Question 5: Longest Substring Without Repeating Characters
# Given a string s, return the length of the longest substring that contains no repeated characters.

# Input:  s = "abcabcbb"
# Output: 3


def longest(s):
    left=0
    seen = {}
    maxlen = 0

    # agar seen me hai and current window ki range me bho to left ko right 
    # ke aage le aayo, us current window se bahr aane ke liye

    for right, char in enumerate(s):
        if char in seen and seen[char] >=left:
            left = seen[char]+1
        
        seen[char] = right
        maxlen = max(maxlen, right-left+1)

    

    return maxlen


