from linked_list_ds.linkedlist import LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedlist = LinkedList()
        
    def test_is_empty(self):
        '''
            unittest for is_empty()
        '''
        self.assertTrue(self.linkedlist.is_empty())
        self.linkedlist.append(1)
        self.assertFalse(self.linkedlist.is_empty())
        self.linkedlist.append(2)
        self.assertFalse(self.linkedlist.is_empty())
        
    def test_append(self):
        '''
            unittest for append(value)
        '''
        self.linkedlist.append(1)
        self.assertEqual(self.linkedlist.length, 1)
        self.linkedlist.append(2)
        self.assertEqual(self.linkedlist.length, 2)
        self.linkedlist.append(3)
        self.assertEqual(self.linkedlist.length, 3)
        
    def test_get_head(self):
        '''
            unittest for get_head()
        '''
        self.linkedlist.append(2)
        self.assertEqual(self.linkedlist.get_head().value, 2)
        self.linkedlist.append(1)
        self.assertEqual(self.linkedlist.get_head().value, 2)
    
    def test_get_tail(self):
        '''
            unittest for get_tail()
        '''
        self.linkedlist.append(1)
        self.assertEqual(self.linkedlist.get_tail().value, 1)
        
        self.linkedlist.append(2)
        self.assertEqual(self.linkedlist.get_tail().value, 2)
        
        self.linkedlist.append(3)
        self.assertEqual(self.linkedlist.get_tail().value, 3)
        
    def test_pop(self):
        '''
            unittest for pop()
        '''
        self.linkedlist.append(1)
        self.linkedlist.append(2)
        self.linkedlist.append(3)
        self.linkedlist.append(4)
        self.linkedlist.pop()
        self.assertEqual(self.linkedlist.get_tail().value, 3)
        
        self.linkedlist.pop()
        self.assertEqual(self.linkedlist.get_tail().value, 2)
        
        self.linkedlist.pop()
        self.assertEqual(self.linkedlist.get_tail().value, 1)
        
        print(self.linkedlist.length)
        
    def test_prepend(self):
        '''
            unittest for prepend(value)
        '''
        self.assertEqual(self.linkedlist.get_head(), None)
        self.linkedlist.prepend(1)
        self.assertEqual(self.linkedlist.get_head().value, 1)
        self.linkedlist.prepend(2)
        self.assertEqual(self.linkedlist.get_head().value, 2)
        self.linkedlist.prepend(3)
        self.assertEqual(self.linkedlist.get_head().value, 3)
        
    def test_pop_first(self):
        '''
            unittest for pop_first()
        '''
        self.linkedlist.append(1)
        self.linkedlist.append(2)
        self.linkedlist.append(3)
        self.linkedlist.append(4)
        self.linkedlist.append(5)
        
        self.linkedlist.pop_first()
        self.assertEqual(self.linkedlist.get_head().value, 2)
        
        self.linkedlist.pop_first()
        self.assertEqual(self.linkedlist.get_head().value, 3)
        
        self.linkedlist.pop_first()
        self.assertEqual(self.linkedlist.get_head().value, 4)
        
    def test_set_node(self):
        '''
            unittest for set_node(index, value)
        '''
        self.linkedlist.append(1)
        self.linkedlist.append(2)
        self.linkedlist.append(3)
        self.linkedlist.append(4)
        self.linkedlist.append(5)
        
        self.linkedlist.set_node(0, 1)
        self.assertEqual(self.linkedlist.get_node(0).value, 1)
        
        self.linkedlist.set_node(1, 11)
        self.assertEqual(self.linkedlist.get_node(1).value, 11)
        
        self.linkedlist.set_node(2, 111)
        self.assertEqual(self.linkedlist.get_node(2).value, 111)
        
        self.linkedlist.set_node(3, 1111)
        self.assertEqual(self.linkedlist.get_node(3).value, 1111)
        
        self.linkedlist.set_node(4, 11111)
        self.assertEqual(self.linkedlist.get_node(4).value, 11111)
        
    
    def test_get_node(self):
        '''
            unittest for get_node(index)
        '''
        self.linkedlist.append(1)
        self.linkedlist.append(2)
        self.linkedlist.append(3)
        self.linkedlist.append(4)
        self.linkedlist.append(5)
        
        for index in range(self.linkedlist.length):
            self.assertEqual(self.linkedlist.get_node(index).value, index + 1)
            
    def test_insert(self):
        '''
            unittest for insert(index, value)
        '''
        for i in range(1, 6, 1):
            self.linkedlist.append(i)
            
        self.linkedlist.insert(0, 1)
        self.assertEqual(self.linkedlist.get_head().value, 1)
        
        self.linkedlist.insert(6, 111111)
        self.assertEqual(self.linkedlist.get_tail().value, 111111)
        
        self.linkedlist.insert(1, 11)
        self.assertEqual(self.linkedlist.get_node(1).value, 11)
        
        self.linkedlist.insert(4, 111)
        self.assertEqual(self.linkedlist.get_node(4).value, 111)
            
        self.linkedlist.print_list()
        
    def test_remove(self):
        '''
            unittest for remove(index)
        '''
        self.linkedlist.append(11)
        self.linkedlist.append(12)
        self.linkedlist.append(13)
        self.linkedlist.append(14)
        self.linkedlist.append(15)
        
        self.linkedlist.remove(0)
        self.assertEqual(self.linkedlist.get_head().value, 12)
        
        self.linkedlist.remove(self.linkedlist.length - 1)
        self.assertEqual(self.linkedlist.get_tail().value, 14)
        
        returned_value = self.linkedlist.remove(1)
        self.assertEqual(returned_value.value, 13)
        
        
    def test_reverse(self):
        '''
            unittest for reverse()
        '''
        self.linkedlist.append(11)
        self.linkedlist.append(12)
        self.linkedlist.append(13)
        self.linkedlist.append(14)
        self.linkedlist.append(15)
        
        self.linkedlist.reverse()
        
        self.assertEqual(self.linkedlist.get_node(0).value, 15)
        self.assertEqual(self.linkedlist.get_node(1).value, 14)
        self.assertEqual(self.linkedlist.get_node(2).value, 13)
        self.assertEqual(self.linkedlist.get_node(3).value, 12)
        self.assertEqual(self.linkedlist.get_node(4).value, 11)

if __name__ == '__main__':
    unittest.main()