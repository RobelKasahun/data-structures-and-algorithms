from linked_list_ds.linkedlist import LinkedList

linkedlist = LinkedList()

# Test for is_empty()
print(linkedlist.is_empty())
linkedlist.append(1)
print(linkedlist.is_empty())

# test for append()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)

# test for get_head()
print(linkedlist.get_head().value)

# test for get_tail()
print(linkedlist.get_tail().value)

# test for pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()

linkedlist.prepend(1)
linkedlist.prepend(2)
linkedlist.prepend(3)
linkedlist.prepend(4)
linkedlist.prepend(5)

# test for print_list
linkedlist.print_list()
# test for length
print(linkedlist.length)