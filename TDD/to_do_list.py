# flake8: noqa
from datetime import datetime


class ToDoList:
    DEFAULT_DATE_FORMAT = '%d/%m/%Y'

    def __init__(self) -> None:
        self.MY_EVENTS: dict = {}

    @classmethod
    def _converting_str_to_date(cls, date: str):
        try:
            return datetime.strptime(date, cls.DEFAULT_DATE_FORMAT)
        except AssertionError:
            raise Exception('Date does not match with the default format.')

    @staticmethod
    def _add_event(title: str, date: str, time: str, description: str | None = None):
        assert isinstance(title, str), 'Title is not an str instance.'
        assert isinstance(date, str), 'Date is not an str instance.'
        assert isinstance(time, str), 'Time is not an str instance.'
        assert isinstance(description, str) or description is None, 'Description is not an str instance or none value.'
        
        return {
            'Title': title,
            'Date': date,
            'Time': time,
            'Description': description,
        }

    def add_event(self, title: str, date: str, time: str, description: str | None = None):
       self.MY_EVENTS[(date + '|' + time)] = __class__._add_event(title, date, time, description)
    
    def remove_event(self, date: str, time: str):
        self.MY_EVENTS.pop(f'{date}|{time}')
        return True
        


if __name__ == '__main__':
    ...
