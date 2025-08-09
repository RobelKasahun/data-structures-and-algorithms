from linkedlist import LinkedList
'''
    - Linked List Data Structure
        - Linked List Big-O
            - append()                  -> Add to the end of the Linked List
                - O(1)

            - pop()                     -> Remove the last node of the Linked List
                - O(n)

            - prepend()                 -> Add a node to the front of the Linked List
                - O(1)
                
            - pop(0)                    -> Remove the front node of the Linked List
                - O(1)
                
            - insert(index, node)       -> Add a node at the given index
                - O(n)
                
            - remove()                  -> Remove a node from the middle of the Linked List
                - O(n)
                
            - search(index)             -> Search a node at the index
                - O(n)
'''

'''
    - Node
        - value
        - A pointer to the next node
'''

head = {
    'value': 1, 
    'next': {
        'value': 2, 
        'next': {
            'value': 3, 
            'next': {
                'value': 4, 
                'next': {
                    'value': 5, 
                    'next': {
                        'value': 6, 
                        'next': {
                            'value': 7, 
                            'next': {
                                'value': 8, 
                                'next': {
                                    'value': 9, 
                                    'next': {
                                        'value': 10, 
                                        'next': None
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

print(head['next']['next']['next']['next']['next']['next']['next']['next']['next']['next'])
print()

'''
    - Construtor
        - Is a special function designed to initialize an instance of a class
'''
class DataStructure:
    def __init__(self, value):
        ''' Constructor / Initializer '''
        self._value = value
print()

linkedlist = LinkedList()
# add nodes
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.append(6)
linkedlist.append(7)
linkedlist.append(8)
linkedlist.append(9)
linkedlist.append(10)
print(linkedlist.length)
print()

# remove the last node of the Linked List
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.pop()
linkedlist.print_list()

print(f'head of the Linked List: {linkedlist.head.value if linkedlist.head else None}')
print(f'tail of the linked list: {linkedlist.tail.value if linkedlist.tail else None}')
print(linkedlist.length)

