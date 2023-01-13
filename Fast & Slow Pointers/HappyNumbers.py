# Given a number, return True if the number is a happy number and false otherwise

# Any number will be called a happy number if,
# after repeatedly replacing it with a number equal to the sum of the square of all of its digits,
# leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

# This is a cycle finding problem so we can use fast & slow pointers
# the number is guaranteed to enter a cycle, so the problem breaks down to determening if the cycle is at 1 or other numbers

def find_happy_number(num):
    fast, slow = num, num
    while True:
        slow = find_square_sum(slow)   # move slow by one step
        fast = find_square_sum(find_square_sum(fast))         # move fast by two steps
        if fast == slow:            # if the pointers collide, the numbers have reached a cycle
            break
    return slow == 1                # if the pointers are at 1, the number is a happy number 

def find_square_sum(num):           # find the sum of the squares of num's digits
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit * digit
        num //= 10
    return sum

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
