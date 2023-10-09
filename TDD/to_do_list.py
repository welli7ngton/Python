# flake8: noqa
from datetime import datetime


class ToDoList:
    DEFAULT_DATE_FORMAT = '%d/%m/%Y'

    @staticmethod
    def add_item(title: str, date: str, time: str, description: str | None = None):
        assert isinstance(title, str), 'Title is not an str instance.'
        assert isinstance(date, str), 'Date is not an str instance.'
        assert isinstance(time, str), 'Time is not an str instance.'
        assert isinstance(description, str) or description is None, 'Description is not an str instance or none value.'
        try:
            converted_date = datetime.strptime(date, __class__.DEFAULT_DATE_FORMAT)
        except AssertionError:
            raise Exception('time data does not march with the default format.')
        return True


if __name__ == '__main__':
    ...
