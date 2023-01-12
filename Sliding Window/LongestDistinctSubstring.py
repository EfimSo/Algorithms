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

def main1():
    print(findDistinctSubstring("aabccbb")) # should be 3
    print(findDistinctSubstring("abbbb")) # should be 2
    print(findDistinctSubstring("abccde")) # should be 3

# main1()

# different approach using a set
def find_distinct_substring(str):
    window_start, window_end= 0, 0
    max_len = 0
    chars = set()
    while window_end < len(str):
        right_char = str[window_end]
        if right_char not in chars:
            chars.add(right_char)
            max_len = max(max_len, len(chars))
            window_end += 1
        else:
            chars.remove(str[window_start])
            window_start += 1
    return max_len

def main2():
    print(find_distinct_substring("aabccbb")) # should be 3
    print(find_distinct_substring("abbbb")) # should be 2
    print(find_distinct_substring("abccde")) # should be 3

main2()