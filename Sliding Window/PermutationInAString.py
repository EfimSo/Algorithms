# Given a string and a pattern, find out if the string contains any permutation of the pattern.


# fixed window size of len(pat)
# make frequency dictionary for window and for pat
# if freq_dict == pat_dict, return True
# else, keep moving right and delete left_char

# my solution using two dictionaries
def hasPermutation(str, pat):
    window_start = 0
    window_dict = dict() # dictionary for char frequencies in window
    pat_dict = dict() # dictionary for char frequencies in pattern
    for c in pat:
        if c not in pat_dict:
            pat_dict[c] = 0
        pat_dict[c] += 1

    for window_end in range(len(str)):
        # add right-most char to window dict
        right_char = str[window_end]
        if right_char not in window_dict:
            window_dict[right_char] = 0
        window_dict[right_char] += 1

        if (window_end - window_start + 1) == len(pat):
            if window_dict == pat_dict:
                return True
            # move right by deleting left-most char
            left_char = str[window_start]
            window_dict[left_char] -= 1
            if window_dict[left_char] == 0:
                del window_dict[left_char]
            window_start += 1

    return False

def test1():
    print(hasPermutation("oidbcaf", "abc")) # True
    print(hasPermutation("odicf", "dc"))    # False
    print(hasPermutation("bcdxabcdy", "bcdyabcdx"))    # True
    print(hasPermutation("aaacb", "abc"))    # True

# test1()

# example solution using one dictionary
def find_permutation(str1, pattern):
    window_start, matched = 0,0
    char_frequency = dict()

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        
        if matched == len(char_frequency):
            return True
        
        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return False

def test2():
    print(find_permutation("oidbcaf", "abc")) # True
    print(find_permutation("odicf", "dc"))    # False
    print(find_permutation("bcdxabcdy", "bcdyabcdx"))    # True
    print(find_permutation("aaacb", "abc"))    # True

test2()