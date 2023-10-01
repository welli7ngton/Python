class Calculator:
    def sum(x: int | float, y: int | float) -> int | float:
        return x + y

    def sub(x: int | float, y: int | float) -> int | float:
        return x - y

    def mult(x: int | float, y: int | float) -> int | float:
        return x * y

    def division(x: int | float, y: int | float) -> int | float:
        try:
            return x // y
        except ZeroDivisionError:
            return '0DivisionError'
