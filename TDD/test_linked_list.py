# flake8: noqa
import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.lkd = LinkedList()
    
    def test_adding_none_value_to_linkedlist_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            self.lkd.add(value=None)
        self.assertEqual(ex.exception.args[0], 'class LinkedList cant accept values diferent of: int, float, str, bool.')

    def test_getting_the_length_of_the_linkedlist(self):
        self.assertEqual(self.lkd.length(), 0)
        
            



if __name__ == '__main__':
    unittest.main(verbosity=2)
