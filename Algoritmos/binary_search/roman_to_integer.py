def romanToInt(s: str) -> int:
    hashNums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    prev = 0
    total = 0

    for i in range(len(s) - 1, -1, -1):
        actual = hashNums.get(s[i])
        if actual >= prev:
            total += actual
            prev = actual
        else:
            total -= actual
    return total


if __name__ == '__main__':
    print(romanToInt('XIV'))
    print(romanToInt('XX'))
    print(romanToInt('XIX'))
