from typing import List
from fractions import Fraction


def bitCount(x: int) -> int:
    cnt = 0
    while x:
        x &= x - 1
        cnt += 1
    return cnt


def fracs(s: int) -> List[Fraction]:
    res = []
    for x in range(1, s):
        y = s - x
        f = Fraction(x, y)
        if f.numerator != x:
            continue
        res.append(f)
    return res


def A(n: int) -> int:
    n //= 4

    cands = []

    cnt = 10
    for s in range(1, 100):
        cands += fracs(s)
        if len(cands) >= n:
            cnt -= 1
            if cnt == 0:
                break
    cands.sort()

    L = 0
    xs = [f.denominator for f in cands]
    xs.sort(reverse=True)
    for i in range(n):
        L += xs[i]
    L *= 2

    res = 10 ** 9
    for k in range(2):
        dp = []
        for i in range(L + 1):
            dp.append([-1] * (n + 1))
        dp[k][k] = 0

        for f in cands:  # 269
            dy = f.numerator * 2
            dx = f.denominator * 2
            for x in range(L - dx, -1, -1):  # 2773
                for i in range(n):  # 250
                    if dp[x][i] < 0:
                        continue

                    nx = x + dx
                    nsz = dp[x][i] + x * dy + dx * dy // 2

                    if 0 <= dp[nx][i + 1] <= nsz:
                        continue

                    dp[nx][i + 1] = nsz

        for x in range(L):
            if dp[x][n] < 0:
                continue
            sz = dp[x][n] + k * x
            res = min(res, sz)

    return res


def test_A():
    assert A(4) == 1
    assert A(8) == 7
    assert A(12) == 25
    assert A(40) == 1039
    assert A(100) == 17473


def main():
    print(A(1000))


if __name__ == "__main__":
    main()