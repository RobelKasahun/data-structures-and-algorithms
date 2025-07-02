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
        

if __name__ == '__main__':
    unittest.main()