# Leetcode: 9 Palindrome Number

def isPalindrome(x):
    x = [n for n in str(x) if n not in "-"]
    left = 0
    right = len(x) - 1

    while left <= right:
        if x[left] != x[right]:
            return False

        if x[left] == x[right]:
            left += 1
            right -= 1
    return True


if __name__ == '__main__':
    print(isPalindrome(-121))
