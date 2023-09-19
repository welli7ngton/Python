import string


class Phone:
    valid_chars = string.digits + '(' + ')'

    def __init__(self, _id: str, number: str) -> None:
        self.list_of_phones = dict()
        self.phones(_id, number)
        return

    def __str__(self) -> str:
        return str(self.list_of_phones)

    def phones(self, _id: str, number: str):
        if self.is_valid(number):
            self.list_of_phones = {
                _id: number
            }

    def is_valid(self, number: str):
        for i in number:
            if i not in Phone.valid_chars:
                raise Exception(
                    f'Caracteres inválidos("{i}") no número cadastrado'
                )
        return True

    def get_id(self):
        key = [_ for _ in self.list_of_phones.keys()]
        return key[0]

    def get_number(self):
        value = [_id for _id in self.list_of_phones.values()]
        return value[0]


class Contact:
    def __init__(self, name: str, favorited: bool = False) -> None:
        self.favorited = favorited
        self.phones: list[Phone] = []
        self.name = name.capitalize()
        return

    def add_phone(self, _id: str, number: str):
        self.phones.append(Phone(_id, number))

    def rm_phone(self, index: int):
        return self.phones.pop(index)

    def toogle_favorited(self):
        self.favorited = True

    def remove_from_favorites(self):
        self.favorited = False

    def get_phones(self):
        print(f"Contacts({self.name})")
        for phone in self.phones:
            print(phone)
        return self.phones

    def get_name(self):
        return self.name


if __name__ == "__main__":
    wellington = Contact('Wellington')
    marilia = Contact('Marília')

    wellington.add_phone('celular', '888a888888')
    wellington.add_phone('casa', '8123123312')
    marilia.add_phone('celular', '5435093405')
    marilia.add_phone('casa', '2222222222')

    wellington.get_phones()

    marilia.rm_phone(0)

    marilia.get_phones()
