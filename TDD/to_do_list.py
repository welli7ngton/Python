# flake8: noqa
from datetime import datetime


class ToDoList:
    DEFAULT_DATE_FORMAT = '%d/%m/%Y'

    @classmethod
    def _converting_str_to_date(cls, date: str):
        try:
            return datetime.strptime(date, cls.DEFAULT_DATE_FORMAT)
        except AssertionError:
            raise Exception('Date does not match with the default format.')

    @staticmethod
    def add_event(title: str, date: str, time: str, description: str | None = None):
        assert isinstance(title, str), 'Title is not an str instance.'
        assert isinstance(date, str), 'Date is not an str instance.'
        assert isinstance(time, str), 'Time is not an str instance.'
        assert isinstance(description, str) or description is None, 'Description is not an str instance or none value.'
        
        return {
            'Title': title,
            'Date': __class__._converting_str_to_date(date),
            'Time': time,
            'Description': description,
        }

        


if __name__ == '__main__':
    ...
