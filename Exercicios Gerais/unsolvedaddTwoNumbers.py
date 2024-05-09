# flake8:noqa
from typing import List, Optional
# Entrada: l1 = [2,4,3], l2 = [5,6,4]
# Saída: [7,0,8]
# Explicação: 342 + 465 = 807.

class Solution:
    @classmethod
    def addTwoNumbers(cls, l1: Optional[List], l2: Optional[List]) -> Optional[List]:
        result: List[int] = []
        right: int|None = None
        for i in range(len(l1)):
            if right:
                result.append(l1[i] + l2[i] + right)
                right = None
            elif l1[i] + l2[i] < 10:
                result.append(l1[i] + l2[i])
            else:
                right = (l1[i] + l2[i]) // 10
                result.append((l1[i] + l2[i]) % 10)
        
        result.reverse()
        return result
        


if __name__ == '__main__':
    print(Solution.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))
    # print(14//10)
    # print(10%10)
