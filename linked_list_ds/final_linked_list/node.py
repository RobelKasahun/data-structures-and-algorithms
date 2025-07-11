class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def create_node(self, value):
        return Node(value)