MOD = 10 ** 9 + 7


def A(k: int, n: int) -> int:
    n = n // k
    fact = [0] * (k + 1)
    for i in range(k + 1):
        fact[i] = 1 if i == 0 else fact[i - 1] * i % MOD
    ifact = [0] * (k + 1)
    for i in range(k, -1, -1):
        ifact[i] = (
            pow(fact[i], MOD - 2, MOD)
            if i == k else ifact[i + 1] * (i + 1) % MOD
        )

    mul2 = pow(pow(2, MOD - 2, MOD), 2 * n, MOD)
    pow2 = pow(2, n * k, MOD)

    res = 0
    for m in range(k // 2 + 1):
        res = (res + fact[k] * ifact[m] * ifact[m]
               * ifact[k - 2 * m] * pow2) % MOD
        pow2 = pow2 * mul2 % MOD
    return res


def test_A():
    assert A(3, 9) == 560
    assert A(4, 20) == 1060870


def main():
    print(A(10 ** 8, 10 ** 16))


if __name__ == "__main__":
    main()
