from linkedlist import LinkedList

linked_list = LinkedList()

# *** test for append *** #
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
print()

# *** Test for pop_last() *** #
print(linked_list.pop_last().value)
print(linked_list.pop_last().value)
print(linked_list.pop_last().value)
print(linked_list.pop_last().value)
print(linked_list.pop_last().value)
print()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print(linked_list.head.value)
print(linked_list.tail.value)
print()

print(linked_list.pop_last().value)
print(linked_list.pop_last().value)
print(linked_list.pop_last().value)
print(linked_list.pop_last().value)
print(linked_list.pop_last().value)
print()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
print()

result = linked_list.pop_last().value
print(result)

result = linked_list.pop_last().value
print(result)

result = linked_list.pop_last().value
print(result)

result = linked_list.pop_last().value
print(result)

result = linked_list.pop_last().value
print(result)
print()

for n in range(1, 11, 1):
    linked_list.append(n)
print()

# *** Test for pop_first() *** #
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print()

# *** Test for prepend() *** #
linked_list.prepend(1)
linked_list.prepend(2)
linked_list.prepend(3)
linked_list.prepend(4)
linked_list.prepend(5)
print()

# *** Test for pop_first() *** #
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print(linked_list.pop_first().value)
print()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# *** Test for get_node(index) *** #
print(linked_list.get_node(0).value)
print(linked_list.get_node(1).value)
print(linked_list.get_node(2).value)
print(linked_list.get_node(3).value)
print(linked_list.get_node(4).value)
print(linked_list.get_node(5))
print(linked_list.get_node(-1))
print()

print(linked_list.get_node(0).value)
print()

# *** Test for set_node() *** #
linked_list.set_node(0, 1)
linked_list.set_node(1, 11)
linked_list.set_node(2, 111)
linked_list.set_node(3, 1111)
linked_list.set_node(4, 11111)
result = linked_list.set_node(5, 111111)
print(result)

result = linked_list.set_node(-10, 1111111)
print(result)
print()

# *** Test for insert() *** #
linked_list.insert(3, 4)
linked_list.insert(0, 101)
linked_list.insert(7, 101)
print()
linked_list.print_linkedlist()
print()

# *** Test for remove() *** #
linked_list.remove(0)
linked_list.remove(0)
linked_list.remove(linked_list.length - 1)
linked_list.remove(linked_list.length - 1)

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.remove(2)
linked_list.remove(3)
linked_list.remove(2)
print()
print()


linked_list.clear()
# test for print_list
linked_list.print_linkedlist()
print(linked_list.head)
print(linked_list.tail)
print(linked_list.length)
print()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_linkedlist()
print(linked_list.length)
print()

# *** Test for reverse() *** #
linked_list.reverse()

linked_list.print_linkedlist()
print(linked_list.head.value, linked_list.tail.value)