from linkedlist import LinkedList

'''
    - Find the middle node
'''
linked_list = LinkedList()
for i in range(1, 11, 1):
    linked_list.append(i)

linked_list.print_list()

def find_middle_node(head):
    # slow and fast points to the head of the List
    slow = head
    fast = head
        
    # empty list
    if not slow:
        return None
    
    # iterate as long as there is a node next to the fast
    while fast.next:
        # move slow half of fast
        slow = slow.next
            
        # move the fast two steps toward the end
        fast = fast.next
        if fast.next:
            fast = fast.next
            
            # middle node of the List
    return slow.value

print(find_middle_node(linked_list.get_head()))