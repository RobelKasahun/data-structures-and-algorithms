class LinkedList:
    # Node
    class Node:
        def __init__(self, value):
            ''' Node constructor / initializer '''
            self.value = value
            self.next = None
    
    def __init__(self):
        ''' Linked List constructor / Initializer '''
        self.head = None
        self.tail = None
        self.length = 0
        
    def print_list(self):
        '''
            - Worst case time complexity
                - O(n)
                
            Print all nodes of the Linked List
        '''
        # point to the head of the linked list
        temp = self.head
        # iterate through the linked list until the temp is None
        while temp:
            # print the value of the node
            if temp.next:
                print(temp.value, end=' ----> ')
            else:
                print(temp.value, end=' ----> None')
            # move the pointer to the next node
            temp = temp.next
        print()
            
    def append(self, value):
        '''
            - Worst case time complexity
                - O(1)
                
            Append to the end or back of the Linked List
        '''
        # New node
        node = self.Node(value)
        
        if not self.head:
            # Linked List is empty
            self.head = self.tail = node
        else:
            # There is at least one node in the List
            # last node points to the new node
            self.tail.next = node
            # make the new node the tail of the List
            self.tail = node
            # The new node or the tail of the List must point to None
            # since it is the end of the List
            self.tail.next = None
        
        # update the length of the Linked List
        self.length += 1
        
        # a node has been added successfully
        return True
    
    def pop(self):
        ''' 
            - Worst case time complexity
                - O(n)

            remove the last node of the
            Linked List and return the removed node
        '''
        temp = None
        
        if not self.head:
            # Empty Linked List
            return None
        
        if self.length == 1:
            '''
                - Best case time complexity
                    - Ω(1)
            '''
            # Only one node
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            
            return temp
        
        # There are more than one nodes in the Linked List
        temp = self.head
        pre = None
        
        while temp.next:
            pre = temp
            temp = temp.next
            
        # pre is the tail of the Linked list
        self.tail = pre
        self.tail.next = None
        
        # decrement the nodes count of the Linked List
        self.length -= 1
        
        # return the removed node
        return temp
    
    
    def prepend(self, value):
        '''
            - Best case time complexity
                - O(1)
        '''
        node = self.Node(value)
        
        # empty list
        if not self.head:
            self.head = self.tail = node
        else:
            # add node to the front of the List
            node.next = self.head
            # make the new node head of the List
            self.head = node
            
        self.length += 1
        
        # a new node has been added to the beginning of the List 
        return True
    
    def pop_first(self):
        '''
            - Time complexity
                - O(1)
        '''
        temp = None
        # Linked List is empty
        if not self.head and not self.tail:
            return temp
        
        # List contains only one node
        if self.length == 1:
            temp = self.head = self.tail
            self.head = self.tail = None
        else:
            # List contains more than one node
            temp = self.head
            self.head = self.head.next
            
        # brake the link
        temp.next = None
        
        self.length -= 1
        return temp
        
    
    