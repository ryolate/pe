MOD = 10 ** 9 + 7


def A(k: int, n: int) -> int:
    n = n // k
    print("A")
    fact = [0] * (k + 1)
    print("A2")
    for i in range(k + 1):
        if i * 100 % k == 0:
            print(f"A: {i}")
        fact[i] = 1 if i == 0 else fact[i - 1] * i % MOD
    print("A3")
    ifact = [0] * (k + 1)
    for i in range(k, -1, -1):
        ifact[i] = (
            pow(fact[i], MOD - 2, MOD) if i == k else ifact[i + 1] * (i + 1) % MOD
        )

    res = 0
    for m in range(k):
        if m * 2 > k:
            break
        if m * 200 % k == 0:
            print(m)
        res = (
            res
            + fact[k]
            * ifact[m]
            * ifact[m]
            * ifact[k - 2 * m]
            * pow(2, n * (k - 2 * m), MOD)
        ) % MOD
    return res


def test_A():
    assert A(3, 9) == 560
    assert A(4, 20) == 1060870


def main():
    print(A(10 ** 8, 10 ** 16))


if __name__ == "__main__":
    main()