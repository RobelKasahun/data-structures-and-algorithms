from linkedlist import LinkedList

linked_list = LinkedList()
print(linked_list.head, linked_list.tail, linked_list.length)
print()

# *** append(value) *** #
linked_list = LinkedList()
append_result = linked_list.append(1)
print(f'append_result: {append_result}')
append_result = linked_list.append(2)
print(f'append_result: {append_result}')
append_result = linked_list.append(3)
print(f'append_result: {append_result}')
append_result = linked_list.append(4)
print(f'append_result: {append_result}')
append_result = linked_list.append(5)
print(f'append_result: {append_result}')
print()

# *** pop() *** #
pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value}')
pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value}')
pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value}')
pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value}')
pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value}')
print()

# head and tail
print(f'head ----> {linked_list.get_head()}')
print(f'tail ----> {linked_list.get_tail()}')

# *** print_list *** #
linked_list.print_list()

# *** length *** #
print(linked_list.length)
