class Calculator:
    def __init__(self, x: int | float, y: int | float) -> None:
        assert isinstance(x, (int, float)), 'x shold be an int or float'
        assert isinstance(y, (int, float)), 'y shold be an int or float'
        self.x = x
        self.y = y

    def sum(self) -> int | float:
        return self.x + self.y

    def sub(self) -> int | float:
        return self.x - self.y

    def mult(self) -> int | float:
        return self.x * self.y

    def division(self) -> int | float:
        try:
            return self.x // self.y
        except ZeroDivisionError:
            raise Exception('0DivisionError')
