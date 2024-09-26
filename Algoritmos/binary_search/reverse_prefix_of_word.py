# Leetcode 2000: Reverse Prefix of Word


def reversePrefix(word, ch):
    prefix = ""
    if ch not in word:
        return word
    for char in word:
        if char != ch:
            prefix += char

        else:
            prefix += char
            break

    left = 0
    right = len(prefix) - 1

    reversed_prefix = ["" for x in range(right + 1)]
    while left <= right:
        reversed_prefix[left], reversed_prefix[right] = prefix[right], prefix[left]
        left += 1
        right -= 1

    reversed_prefix = "".join([x for x in reversed_prefix])

    return reversed_prefix + word[len(prefix) :]


if __name__ == "__main__":
    print(reversePrefix("abcdefd", "d"))
