
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, r: int) -> str:
        res = []
        cnt = Counter(s)
        arr = []
        for k, v in cnt.items():
            arr.append([k, v])
        arr.sort(reverse=True)
        cur = 0
        while arr:
            print(arr)
            if cur == r and len(arr) == 1:
                break
            if cur < r:
                res.append(arr[0][0])
                arr[0][1] -= 1
                cur += 1
                if arr[0][1] == 0:
                    arr.pop(0)
                    cur = 0
            else:
                cur = 0
                res.append(arr[1][0])
                arr[1][1] -= 1
                if arr[1][1] == 0:
                    arr.pop(1)
        return ''.join(res)  

s = Solution()
print(s.repeatLimitedString('cczazcc',3))



