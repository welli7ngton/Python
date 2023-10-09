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
            ToDoList.add_item(0, '11/11/1111', '00:00', None)
        self.assertEqual(ex.exception.args[0], 'Title is not an str instance.')

    def test_if_date_is_an_str_instance_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            ToDoList.add_item('title', 1, '00:00', None)
        self.assertEqual(ex.exception.args[0], 'Date is not an str instance.')

    def test_if_time_is_an_str_instance_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            ToDoList.add_item('title', '11/11/1111', 0, None)
        self.assertEqual(ex.exception.args[0], 'Time is not an str instance.')


    def test_if_description_is_an_str_instance_or_none_value_getting_an_assertion_error(self):
        with self.assertRaises(Exception) as ex:
            ToDoList.add_item('title', '11/11/1111', '00:00', 0)
        self.assertEqual(ex.exception.args[0], 'Description is not an str instance or none value.')

    def test_if_date_can_be_converted_to_datetime_with_strptime_function_raises_an_error(self):
        with self.assertRaises(Exception) as ex:
            self.assertEqual(ToDoList.add_item('test_item', '11|11|1111', '00:00', None), 'time data does not march with the default format.')


if __name__ == '__main__':
    unittest.main(verbosity=2)