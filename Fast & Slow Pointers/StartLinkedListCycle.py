# Given the head of a Singly LinkedList that contains a cycle,
# write a function to find the starting node of the cycle.

class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


# same solution as find_cycle_2 but simplified code
# start at the beginning and detect the cycle using fast, slow pointers
# at meeting point, initialize a new pointer set at head
# move slow and new pointer at the same speed until they point to the same node
# the meeting point is the start of the cycle
# why this works: https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/
def find_cycle_start(head: Node):
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:    # reached intersection point
            pointer = head  # new pointer to iterate from the beginning
            while pointer is not slow:  # check if slow and new pointer met
                pointer = pointer.next
                slow = slow.next
            return pointer
    return None


  
# driver code: detects cycle using fast, slow pointers then calls functions to calculate length and start
def find_cycle_start_2(head: Node):
    cycle_length = 0
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            cycle_length = find_cycle_length(slow)
            break
    return find_start(head, cycle_length)
    
# runs slow through one cycle of the loop while incrementing length
def find_cycle_length(slow):
    cycle_length = 0
    temp = slow
    while temp is not None:
        cycle_length += 1
        temp = temp.next
        if temp is slow:        # reached the node it started with
            break
    return cycle_length

# starts with two pointers, one cycle_length ahead of the other
# increments the pointers by one
# when p2 completes one cycle, p1 will be just entering the cycle
# the point where p1 and p2 point to the same Node is the start of the cycle
def find_start(head, cycle_length):
    p1, p2 = head, head
    # move p2 ahead by cycle_length nodes
    while p2 is not None and cycle_length > 0:
        p2 = p2.next
        cycle_length -= 1
    # increment both pointers until they point to the same node
    while p1 is not p2:
        p1 = p1.next
        p2 = p2.next
    return p1

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()


def main2():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start_2(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start_2(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start_2(head).value))


# main2()
