# flake8: noqa
# To-Do List
# Construa um aplicativo de lista de tarefas (To-Do List)
# com testes para adicionar, remover e marcar tarefas como concluídas.
import unittest
from to_do_list import ToDoList


class TestToDoList(unittest.TestCase):
    # type checking tests
    def test_if_title_is_an_str_instance_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            ToDoList._add_event(0, '11/11/1111', '00:00', None)
        self.assertEqual(ex.exception.args[0], 'Title is not an str instance.')

    def test_if_date_is_an_str_instance_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            ToDoList._add_event('title', 1, '00:00', None)
        self.assertEqual(ex.exception.args[0], 'Date is not an str instance.')

    def test_if_time_is_an_str_instance_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            ToDoList._add_event('title', '11/11/1111', 0, None)
        self.assertEqual(ex.exception.args[0], 'Time is not an str instance.')

    def test_if_description_is_an_str_instance_or_none_value_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            ToDoList._add_event('title', '11/11/1111', '00:00', 0)
        self.assertEqual(ex.exception.args[0], 'Description is not an str instance or none value.')

    def test__converting_str_to_date_function_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            self.assertEqual(ToDoList._add_event('test_item', '1111/11/11', '00:00', None), 'Date does not match with the default format.')
    
    def test_creating_a_dictionare_for_each_event(self):
        self.assertTrue(isinstance(ToDoList._add_event('event test', '11/11/1111', '00:00', 'a test event'), dict))
    
    def test_remve_item_of_the_list(self):
        tdl = ToDoList()
        tdl.add_event('Event Test', '13/10/2023', '15:12')
        self.assertTrue(tdl.remove_event('13/10/2023', '15:12'))


if __name__ == '__main__':
    unittest.main(verbosity=2)