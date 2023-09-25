def regressive_sum(n: int):
    if n == 0:
        return n
    return n + regressive_sum(n - 1)


print(regressive_sum(10))
print(regressive_sum(7))
