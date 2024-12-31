from typing import List


def longest_common_prefix(strs: List[str]):
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]

    return res


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
