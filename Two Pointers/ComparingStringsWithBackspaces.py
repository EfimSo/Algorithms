# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

# Set up two pointers at the end of each string
# iterate backwards and compare the characters at each step
# if char == '#', skip the next char

def backspace_compare(str1, str2):
    p1 = len(str1) - 1
    p2 = len(str2) - 1
    while p1 >= 0 and p2 >= 0:
        p1 = get_next_valid_index(str1, p1)
        p2 = get_next_valid_index(str2, p2)
        if p1 < 0 and p2 < 0:
            return True
        if p1 < 0 or p2 < 0:
            return False
        if str1[p1] != str2[p2]:
            return False
        p1 -= 1
        p2 -= 1
    
    return True

def get_next_valid_index(str, i):
    backspace_count = 0
    while i >= 0:
        if str[i] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        i -= 1
    return i


def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
