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

for n in range(1, 6, 1):
    linked_list.append(n)

# *** get(index) *** #
for n in range(6):
    print(linked_list.get(n).value if linked_list.get(n) else None)
print()

# *** set_node(index, value) *** #
value = '1'
for n in range(5):
    linked_list.set_node(n, int(value))
    value += '1'
print()

# *** insert(index, value) *** #
linked_list.insert(2, 2)
linked_list.insert(0, 0)
linked_list.insert(linked_list.length, 101)
linked_list.insert(6, 101)
print()


# *** remove(index) *** #
remove_result = linked_list.remove(0)
print(f'remove_result = {remove_result.value}')

remove_result = linked_list.remove(linked_list.length)
print(f'remove_result = {remove_result}')

remove_result = linked_list.remove(2)
print(f'remove_result = {remove_result.value}')

remove_result = linked_list.remove(4)
print(f'remove_result = {remove_result.value}')

remove_result = linked_list.remove(linked_list.length - 1)
print(f'remove_result = {remove_result.value}')
linked_list.print_list()
print()

# *** reverse() *** #
linked_list.reverse()
linked_list.print_list()
print()

linked_list.reverse()
print()

linked_list.insert(5, 101)


# head and tail
print(f'head node ----> {linked_list.get_head()}')
print(f'tail node ----> {linked_list.get_tail()}')

# *** print_list *** #
linked_list.print_list()

# *** length *** #
print(f'length: {linked_list.length}')
