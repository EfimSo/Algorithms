# given string s
# find the longest substring with no more than k distinct characters

def findKSubstring(str, k):
    window_start, max_len = 0, 0
    char_freq = dict()

    for window_end in range(len(str)):
        # grow window by adding char
        right_char = str[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        
        # shrink window until no more than k distinct chars
        while len(char_freq) > k:
            # delete char at window_start
            left_char = str[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)
    
    return max_len

print(findKSubstring("araaci", 2)) # should be 4
print(findKSubstring("araaci", 1)) # should be 2
print(findKSubstring("cbbebi", 3)) # should be 5


        

