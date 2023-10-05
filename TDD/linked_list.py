# flake8: noqa
from collections.abc import Iterator


class LinkedList(list):
    def add(self, value: int | float | str | bool):
        assert isinstance(value, (int, float, str, bool)), 'class LinkedList cant accept values diferent of: int, float, str, bool.'
        self.append(value)

    def length(self):
        return len(self)

    def get_this(self, index: int):
        return self[index]

    def delete_this(self, index: int):
        if self[index]:
            self.pop(index)
            return True
        return False

if __name__ == '__main__':
    ...