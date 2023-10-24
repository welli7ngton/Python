class ReverseString:
    @classmethod
    def reverse(cls, s: str):
        return ''.join([s[i - 1] for i in range(len(s), 0, -1)])


def reverse_str(_string: str) -> str:
    return ''.join([_string[i - 1] for i in range(len(_string), 0, -1)])


if __name__ == '__main__':
    print(reverse_str('wellington'))

    print(ReverseString.reverse('): oot skrow ti'))
