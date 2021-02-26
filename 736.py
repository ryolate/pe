from typing import Tuple, List


def recur(i: int, j: int, r: int) -> Tuple[bool, List[bool]]:
    if i == 0 and j == 0:
        return (r == 0, [])
    if i < 0 or j < 0:
        return (False, None)

    left = i - (j << i)
    right = (i << j) - j
    if left <= r <= right:
        ok, v = recur(i - 1, j, r - (1 << j))
        if ok:
            return (True, [True] + v)
        ok, v = recur(i, j - 1, r + (1 << i))
        if ok:
            return (True, [False] + v)
    return (False, None)


def main():
    a = 45
    for i in range(50):
        for j in range(50):
            if (i + j) % 2 != 0:
                continue
            mid = ((1 << i) - (1 << j + 1)) * a
            left = i - (j << i)
            right = (i << j) - j

            if left <= mid <= right:
                print(i, j, left, mid, right)

    n = 46
    for n in range(46, 50):
        ok, v = recur(n, n, a << n)
        if not ok:
            continue
        a = a
        b = a * 2
        for x in v:
            if x:
                a, b = a + 1, b * 2
            else:
                a, b = a * 2, b + 1
        print(a, b)


if __name__ == "__main__":
    main()
