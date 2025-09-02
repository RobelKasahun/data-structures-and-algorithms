from linkedlist import LinkedList

linked_list = LinkedList()
print(linked_list.head, linked_list.tail, linked_list.length)
print()

# *** append(value) *** #
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# *** length *** #
print(linked_list.length)

# head and tail
print(f'head ----> {linked_list.head.value}')
print(f'tail ----> {linked_list.tail.value}')

# *** print_list *** #
linked_list.print_list()
