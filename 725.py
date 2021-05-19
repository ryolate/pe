MOD = 10 ** 16


def S(n: int) -> int:
    # dp[sum][max] -> tot, cnt
    dp = [[(0, 0)] * 10 for _ in range(20)]
    dp[0][0] = (0, 1)

    for _ in range(n):
        ndp = [[(0, 0)] * 10 for _ in range(20)]
        for j in range(10):
            for s in range(20):
                for m in range(10):
                    ns = s + j
                    nm = max(m, j)
                    if ns >= 20:
                        continue

                    tot, cnt = dp[s][m]
                    ntot, ncnt = ndp[ns][nm]

                    ndp[ns][nm] = ((ntot + tot * 10 + j * cnt) % MOD,
                                   (ncnt + cnt) % MOD)
        dp = ndp
    res = 0
    for m in range(10):
        res += dp[m*2][m][0]
    return res % MOD


def test_S():
    assert S(3) == 63270
    assert S(7) == 85499991450


def main():
    print(S(2020))


if __name__ == "__main__":
    main()
