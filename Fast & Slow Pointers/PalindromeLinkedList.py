# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

class Node:
    def __init__(self, val, next = None):
        self.value = val
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, " ", end='')
            temp = temp.next
        print()



def is_palindromic_linked_list(head):
    # if Linked List is zero or one nodes, it is a palindrome
    if head is None or head.next is None:
        return True
    
    # find middle of the linked list
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    # slow is at the middle of the linked list
    # reverse the second half of the linked list to compare with the first half
    head_second_half = reverse(slow)
    copy_head_second_half = head_second_half    # store copy of head for the second half to later reverse back

    # compare the first and second half
    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break
        head = head.next
        head_second_half = head_second_half.next
    
    reverse(copy_head_second_half)      # reverse second half to restore the original linked list

    if head is None or head_second_half is None:    # made it to the end of either half of the LL so halves match
        return True

    return False

# function to revese a linked list (used to reverse second half)
def reverse(head):  
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)
  head.print_list()
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))
  head.print_list()       # check if code restores the LL correctly
  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()