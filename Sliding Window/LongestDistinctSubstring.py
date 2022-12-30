# Given a string, find the length of the longest substring, which has all distinct characters.

def findDistinctSubstring(str):
    window_start, max_len = 0,0
    char_ind = dict() # a dictionary to map chars to their latest seen index

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_ind:
            # if char seen before, skip by either 1 + previous index (if in window)
            # or window_start if already outside window
            window_start = max(window_start, char_ind[right_char] + 1) 
        char_ind[right_char] = window_end # store last index of right_char
    
        max_len = max(max_len, window_end - window_start + 1)

    return max_len

print(findDistinctSubstring("aabccbb")) # should be 3
print(findDistinctSubstring("abbbb")) # should be 2
print(findDistinctSubstring("abccde")) # should be 3