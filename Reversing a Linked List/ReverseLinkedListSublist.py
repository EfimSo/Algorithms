# Given the head of a LinkedList and two positions ‘p’ and ‘q’ (inclusive indeces starting at 0), 
# reverse the LinkedList from position ‘p’ to ‘q’.

# Algorithm:
# 1. Skip the first p-1 nodes, to reach the node at position p.
# 2. Remember the node at position p-1 to be used later to connect with the reversed sub-list
#    and the node at position p to connect with the [q + 1: ] part of the list
#    (first node of the sublist will become last once reversed)
# 3. Reverse the nodes from p to q
# 4. Connect the p-1 and q+1 nodes to the reversed sub-list.


class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

def reverse_sublist(head, p, q):
    if p == q:
        return head
    
    i = 0
    prev, curr, next = None, head, None
    # skip p - 1 nodes for curr to point to pth node
    while curr is not None and i < p:
        prev = curr
        curr = curr.next
        i += 1
    # remember last node before p (at p - 1)
    last_node_first_part = prev
    # remember first node of sublist (at p, will be last once reversed)
    last_node_sublist = curr

    # reverse sublist
    while curr is not None and i < q + 1:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1
    
    # connect list before p with first node of reversed sublist
    if last_node_first_part is not None:
        last_node_first_part.next = prev
    else:
        head = prev     # case where p == 0 (reversed sublist includes head)
    
    last_node_sublist.next = curr   # connect last node of reversed sublist with node at q + 1
    
    return head 
    

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sublist(head, 1, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()


    
    