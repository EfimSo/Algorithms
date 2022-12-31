# Given a string and a pattern, find all anagrams of the pattern in the given string. (rearangements/permutations)
# Return a list of starting indices of the anagrams

# sliding window of fixed length of len(pattern)
# make dictionary for pattern
# make matched variable, subtract from dictionary every time a letter matched
# if a letter completely matched, matched += 1, append window_start to list

def findAllPermuts(str, pattern):
    window_start, matched = 0, 0
    res_list = []
    pat_dict = dict()
    for c in pattern:
        if c not in pat_dict:
            pat_dict[c] = 0
        pat_dict[c] += 1
    
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in pat_dict:
            pat_dict[right_char] -= 1
            if pat_dict[right_char] == 0:
                matched += 1
        
        if matched == len(pat_dict):
            res_list.append(window_start)
        
        # shrink window
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            if pat_dict[left_char] == 0:
                matched -= 1
            pat_dict[left_char] += 1
            window_start += 1
    return res_list

def main():
    print(findAllPermuts("ppqp", "pq"))
    print(findAllPermuts("abbcabc", "abc"))


main()

