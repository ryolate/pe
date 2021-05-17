from bisect import bisect
from functools import lru_cache


fibs = [1, 2]
while fibs[-1] < 23416728348467685:
    fibs.append(fibs[-1] + fibs[-2])


@lru_cache
def G(n: int) -> int:
    if n == 0:
        return 0
    i = bisect(fibs, n)
    fib = fibs[i-1]
    res = G(n-1) + n if fib == n else G(fib) + G(n - fib)
    return res


def test_G():
    assert G(13) == 43


def main():
    print(G(23416728348467685))


if __name__ == '__main__':
    main()
