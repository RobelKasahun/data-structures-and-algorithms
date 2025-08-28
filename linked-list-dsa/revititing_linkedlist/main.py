from linkedlist import LinkedList

linked = LinkedList()

# --- append() [ PASS ] --- #
linked.append(1)
linked.append(2)
linked.append(3)
linked.append(4)
linked.append(5)

# --- print_list [ PASS ] --- #
linked.print_list()
print(linked.head.value, linked.tail.value)
print(linked.length)
print()

# --- pop_first() --- #
linked.pop_first()
linked.pop_first()
linked.pop_first()
linked.pop_first()
linked.pop_first()
linked.pop_first()
print(linked.head.value if linked.head else None, linked.tail.value if linked.tail else None)
print(linked.length)
print()

# --- pop() --- #
for i in range(1, 11, 1):
    linked.append(i)
    
data = linked.pop()
data = linked.pop()
data = linked.pop()
data = linked.pop()
data = linked.pop()
data = linked.pop()
data = linked.pop()
data = linked.pop()
data = linked.pop()
data = linked.pop()
print(f'data = {data.value}')
print(linked.head.value if linked.head else None, linked.tail.value if linked.tail else None)
linked.print_list()
print(linked.length)
print()

# --- prepend(value) --- #
for i in range(1, 11):
    linked.append(i)
linked.prepend(0)

for n in range(1, 11, 1):
    linked.prepend(-n)
linked.print_list()
print(f'length: {linked.length}')
print()

# --- get(index) --- #
for n in range(linked.length):
    print(n, linked.get(n).value)
linked.print_list()
print(f'length: {linked.length}')
print()

value = 1
for n in range(linked.length):
    linked.set_node(n, value)
    value += 1
linked.print_list()
print(f'length: {linked.length}')
print()

# --- insert(index, value) --- #
linked.insert(0, 101)
linked.insert(linked.length, 101)
linked.insert(6, 101)
linked.insert(11, 101)
linked.insert(11, 102)
linked.print_list()
print(f'length: {linked.length}')
print()

# --- remove(index) --- #
linked.remove(0)
linked.remove(5)
linked.remove(9)
linked.remove(9)
linked.remove(21)
linked.remove(20)
linked.remove(19)
linked.remove(11)

for i in range(10, 18):
    linked.remove(10)
linked.print_list()
print(f'length: {linked.length}')
print()

# --- reverse() --- #
linked.print_list()
linked.reverse()
linked.print_list()
print(f'length: {linked.length}')