# Given a string, return the first character that appears exactly once. 
# Return None if no such character exists.
# Example: apple → a
# Try solving in \(O(n)\) time.

def nonrep(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i,0) +1

    for char in s:
        if freq[char] == 1:
            return char
    return None
    


    
