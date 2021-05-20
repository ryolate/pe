# from collections import deque
from typing import List

MOD = 10 ** 16


def cubefuls(n: int) -> List[int]:
    n3 = 0
    while n3**3 < n:
        n3 += 1

    is_prime = [True] * n3
    is_prime[0] = is_prime[1] = False
    for i in range(n3):
        if not is_prime[i]:
            continue
        for j in range(i+i, n3, i):
            is_prime[j] = False
    primes = []
    for i in range(n3):
        if is_prime[i]:
            primes.append(i)

    m = len(primes)

    res = []

    def dfs(d: int, i: int):
        res.append(d)
        for j in range(i, m):
            p = primes[j]
            nd = d * (p ** 3)
            if nd > n:
                break
            while nd <= n:
                dfs(nd, j+1)
                nd *= p
    dfs(1, 0)
    return res


def S(n: int) -> int:
    res = 0
    for d in cubefuls(n):
        res += n // d
    return res


def test_S():
    assert S(16) == 19
    assert S(100) == 126
    assert S(10000) == 13344


def main():
    print(S(10**18))


if __name__ == "__main__":
    main()
