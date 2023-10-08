# flake8: noqa
# To-Do List
# Construa um aplicativo de lista de tarefas (To-Do List)
# com testes para adicionar, remover e marcar tarefas como concluídas.
import unittest
from to_do_list import ToDoList


class TestToDoList(unittest.TestCase):
    def test_return_of_add_item_function(self):
        self.assertTrue(ToDoList.add_item('test', 'a', 'b', 'd'))



if __name__ == '__main__':
    unittest.main(verbosity=2)