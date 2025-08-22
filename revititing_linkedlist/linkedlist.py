'''
    Linked List
'''
class LinkedList:
    class Node:
        '''
            Node Constructor / Initializer
        '''
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
        
    # append(value)
    def append(self, value):
        node = self.Node(value)
        '''
            Adds a new node to the end or tail of the Linked List
            Time complexity
                - O(1)
        '''
        # empty Linked List
        if not self.head and not self.tail:
            self.head = self.tail = node
        else:
            # There are more than one nodes in the Linked List
            self.tail.next = node
            self.tail = node
            self.tail.next = None
        
        self.length += 1
        
        return True
    
    # print_list()
    def print_list(self):
        '''
            Prints all nodes of the Linked List
            Time complexity
                - O(n)
        '''
        # Empty Linked List
        if not self.head and not self.tail:
            print(f'Empty Linked List')
        
        temp = self.head
        while temp:
            if temp.next:
                print(temp.value, end=' ----> ')
            else:
                print(temp.value, end=' ----> None')

            temp = temp.next
        
        print()
        
    # pop_first()
    def pop_first(self):
        '''
            - Removes the first node from the Linked List
            - Time complexity
                - O(1)
        '''
        temp = None
        
        # empty Linked List
        if not self.head and not self.tail:
            return temp
        
        # Linked List contains only one node
        if self.length == 1:
            temp = self.head = self.tail
            self.head = self.tail = None
            self.length -= 1
            return temp
        
        # Linked List contains more than one nodes
        temp = self.head
        self.head = self.head.next
        
        temp.next = None
        
        self.length -= 1
        return temp
    
    # pop_last()
    def pop(self):
        '''
            - Removes a node at the end of a Linked List
            - Time complexity
                - O(n)
        '''
        
        temp = None
        # empty list
        if not self.head and not self.tail:
            return temp
        
        # Linked List contains only one node
        if self.length == 1:
            temp = self.head = self.tail
            self.head = self.tail = None
            self.length -= 1
            return temp
        
        # Linked List contains some nodes
        prev = self.head
        temp = self.head.next
        
        while temp.next:
            prev = temp
            temp = temp.next
            
        self.tail = prev
        self.tail.next = None
        
        self.length -= 1
        
        return temp
    
    def prepend(self, value):
        '''
            Add to the beginning of the Linked List
            Time complexity:
                - O(1)
        '''
        node = self.Node(value)
        # When the List is empty
        if not self.head and not self.tail:
            self.head = self.tail = node
        else:
            # The List contains one or more nodes
            node.next = self.head
            self.head = node
        
        self.length += 1
        
        return True
    
    def get(self, index):
        '''
            Returns the node at the given or specified index
            Time complexity
                - O(n)
        '''
        
        # empty list
        if not self.head and not self.tail:
            return None
        
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
            
        return temp
    
    def set_node(self, index, value):
        '''
            Update the value of the node at the specified or given index
            Time complexity
                - O(n)
        '''
        # empty Linked List
        if not self.head or not self.tail:
            return False
        
        # index out of range
        if index < 0 or index >= self.length:
            return False
        
        # advance the pointer to the position at index
        temp = self.head
        for _ in range(index):
            temp = temp.next
            
        temp.value = value
        
        return True
    
    def insert(self, index, value):
        '''
            Insert a new node before the given or specified index
            Time complexity
                - O(n)
        '''
        # empty list
        if not self.head and not self.tail:
            return False
        
        # index out of range
        if index < 0 or index > self.length:
            return False
        
        # insert the node at the beginning of the Linked List
        if index == 0:
            return self.prepend(value)
        
        # insert the node at the end of the Linked List
        if index == self.length:
            return self.append(value)
        
        # insert the node in the middle of the Linked List
        node = self.Node(value)
        
        prev = self.get(index - 1)
        target = prev.next
        
        node.next = target
        prev.next = node
        
        self.length += 1
        
        return True
        
        
    
    def remove(self, index):
        '''
            Removes a node at the specified or given index
            Time complexity
                - O(n)
        '''
        
        # empty List
        if not self.head and not self.tail:
            return None
        
        # index out of range
        if index < 0 or index >= self.length:
            return None
        
        # remove head
        if index == 0:
            return self.pop_first()
        
        # remove tail
        if index == self.length - 1:
            return self.pop()
        
        # remove a node in the middle of the Linked List
        prev = self.get(index - 1)
        target = prev.next
        
        prev.next = target.next
        
        target.next = None
        
        self.length -= 1
        
        return target
    
    def reverse(self):
        # empty List
        if not self.head and not self.tail:
            return None
        
        # swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        after = None
        before = None
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        