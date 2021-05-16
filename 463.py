from functools import lru_cache


MOD = 1_000_000_000


@lru_cache
def f(n: int) -> int:
    if n == 1:
        return 1
    if n == 3:
        return 3
    if n % 2 == 0:
        return f(n // 2)
    if n % 4 == 1:
        return (2 * f(n // 4 * 2 + 1) - f(n // 4)) % MOD
    if n % 4 == 3:
        return (3 * f(n // 4 * 2 + 1) - 2 * f(n // 4)) % MOD
    return 0


@lru_cache
def O(n: int) -> int:
    if n % 4 > 0:
        if n % 2 == 0:
            return O(n-1)
        return f(n) + O(n-1)

    if n == 0:
        return 0

    a = n // 4
    res = 4
    res += 5 * (O(2 * a - 1) - 1) - 3 * S(a-1)
    return res % MOD


@lru_cache
def E(n: int) -> int:
    if n % 2 > 0:
        return E(n - 1)
    if n == 0:
        return 0
    return S(n // 2)


def S(n: int) -> int:
    return (E(n) + O(n)) % MOD


def test_S():
    assert S(8) == 22
    assert S(100) == 3604


def main():
    print(S(3 ** 37))


if __name__ == "__main__":
    main()
