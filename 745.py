import math

MOD = 10 ** 9 + 7


def S(N: int) -> int:
    n = math.ceil(math.sqrt(N))

    res = 0
    c = [0] * (n + 1)
    for i in range(n, 0, -1):
        c[i] = N // (i * i)
        for j in range(i * 2, n + 1, i):
            c[i] -= c[j]
        res += i * i * c[i]
    return res % MOD


def test_S():
    assert S(10) == 24
    assert S(100) == 767


def main():
    print(S(10 ** 14))


if __name__ == "__main__":
    main()
