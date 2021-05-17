MOD = 1020202009


def inv(a: int) -> int:
    return pow(a, MOD - 2, MOD)


def f(n: int) -> int:
    fact = [1] * (n + 1)
    for i in range(n):
        fact[i+1] = (i+1) * fact[i] % MOD
    ifact = [inv(fact[n])] * (n + 1)
    for i in reversed(range(n)):
        ifact[i] = ifact[i+1] * (i+1) % MOD

    def C(n: int, k: int) -> int:
        return fact[n] * ifact[k] * ifact[n-k]

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(1, n):
        if i % 1000 == 0:
            print('.')
        for k in range(i+1):
            dp[i+1] += dp[i-k] * dp[k] * C(i, k)
            dp[i+1] %= MOD
        dp[i+1] = dp[i+1] * inv(2) % MOD

    return dp[n]


def test_f():
    assert f(4) == 5
    assert f(8) == 1385


def main():
    for i in range(1, 10):
        print(f"{i} => {f(i)}")
    print(f(24680))


if __name__ == '__main__':
    main()
