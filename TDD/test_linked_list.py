# flake8: noqa
"""
Lista Encadeada

Crie uma classe que represente uma lista encadeada. Escreva testes para adicionar, remover e pesquisar elementos na lista.
"""
import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.lkd = LinkedList()
        self.lkd.add('wellington')
    
    def test_adding_none_value_to_linkedlist_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            self.lkd.add(value=None)
        self.assertEqual(ex.exception.args[0], 'class LinkedList cant accept values diferent of: int, float, str, bool.')

    def test_getting_the_length_of_the_linkedlist(self):
        self.assertEqual(self.lkd.length(), 1)
    
    def test_getting_an_value_from_the_list(self):
        self.assertEqual(self.lkd.get_this(0), 'wellington')
    
    def test_deleting_an_list_item_getting_a_true_value(self):
        self.assertTrue(self.lkd.delete_this(0))

    def test_deleting_an_list_item_getting_a_IndexError(self):
        with self.assertRaises(IndexError) as ex:
            self.lkd.delete_this(7)
        self.assertEqual(ex.exception.args[0], 'list index out of range')

        
if __name__ == '__main__':
    unittest.main(verbosity=2)
