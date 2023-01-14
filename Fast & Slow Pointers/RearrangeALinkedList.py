# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that
# the nodes from the second half of the LinkedList are inserted alternately
# to the nodes from the first half in reverse order.
# input:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# output: 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()

# algorithm: 
#   1. find the middle of the LL
#   2. reverse the second half of the LL
#   3. merge the two halves alternating between first and second
def reorder(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    # slow now points at the middle node of the LL
    # reverse second half of the LL
    head_second_half = reverse(slow)
    head_first_half = head 
    # insert nodes alternating between first and second half
    while head_first_half is not None and head_second_half is not None:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp
        
        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp
    # make last node None
    if head_first_half is not None:
        head_first_half.next = None

    return head


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
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    reorder(head)
    head.print_list()



main()