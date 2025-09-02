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
print(f'pop_result: {pop_result.value if pop_result else 'None'}')

pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value if pop_result else 'None'}')

pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value if pop_result else 'None'}')

pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value if pop_result else 'None'}')

pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value if pop_result else 'None'}')

pop_result = linked_list.pop()
print(f'pop_result: {pop_result.value if pop_result else 'None'}')
print()

# *** prepend() *** #
prepend_result = linked_list.prepend(1)

print(f'prepend_result: {prepend_result}')
prepend_result = linked_list.prepend(2)

print(f'prepend_result: {prepend_result}')
prepend_result = linked_list.prepend(3)

print(f'prepend_result: {prepend_result}')
prepend_result = linked_list.prepend(4)

print(f'prepend_result: {prepend_result}')
prepend_result = linked_list.prepend(5)

print(f'prepend_result: {prepend_result}')
print()

# *** pop_first() *** #
pop_first_result = linked_list.pop_first()
print(f'pop_first_result: {pop_first_result.value if pop_first_result else 'None'}')

pop_first_result = linked_list.pop_first()
print(f'pop_first_result: {pop_first_result.value if pop_first_result else 'None'}')

pop_first_result = linked_list.pop_first()
print(f'pop_first_result: {pop_first_result.value if pop_first_result else 'None'}')

pop_first_result = linked_list.pop_first()
print(f'pop_first_result: {pop_first_result.value if pop_first_result else 'None'}')

pop_first_result = linked_list.pop_first()
print(f'pop_first_result: {pop_first_result.value if pop_first_result else 'None'}')

pop_first_result = linked_list.pop_first()
print(f'pop_first_result: {pop_first_result.value if pop_first_result else 'None'}')

print()

# head and tail
print(f'head node ----> {linked_list.get_head()}')
print(f'tail node ----> {linked_list.get_tail()}')

# *** print_list *** #
linked_list.print_list()

# *** length *** #
print(f'length: {linked_list.length}')
