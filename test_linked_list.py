from linked_list_ds.linkedlist import LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedlist = LinkedList()
        
    def test_is_empty(self):
        self.assertTrue(self.linkedlist.is_empty())
        self.linkedlist.append(1)
        self.assertFalse(self.linkedlist.is_empty())
        self.linkedlist.append(2)
        self.assertFalse(self.linkedlist.is_empty())
        
    def test_append(self):
        self.linkedlist.append(1)
        self.assertEqual(self.linkedlist.length, 1)
        self.linkedlist.append(2)
        self.assertEqual(self.linkedlist.length, 2)
        self.linkedlist.append(3)
        self.assertEqual(self.linkedlist.length, 3)
        
    def test_get_head(self):
        self.linkedlist.append(2)
        self.assertEqual(self.linkedlist.get_head().value, 2)
        self.linkedlist.append(1)
        self.assertEqual(self.linkedlist.get_head().value, 2)
    
    def test_get_tail(self):
        self.linkedlist.append(1)
        self.assertEqual(self.linkedlist.get_tail().value, 1)
        
        self.linkedlist.append(2)
        self.assertEqual(self.linkedlist.get_tail().value, 2)
        
        self.linkedlist.append(3)
        self.assertEqual(self.linkedlist.get_tail().value, 3)
        
    def test_pop(self):
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
        self.assertEqual(self.linkedlist.get_head(), None)
        self.linkedlist.prepend(1)
        self.assertEqual(self.linkedlist.get_head().value, 1)
        self.linkedlist.prepend(2)
        self.assertEqual(self.linkedlist.get_head().value, 2)
        self.linkedlist.prepend(3)
        self.assertEqual(self.linkedlist.get_head().value, 3)
        # self.linkedlist.print_list()
        
    def test_pop_first(self):
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
        
        self.linkedlist.print_list()
        

if __name__ == '__main__':
    unittest.main()