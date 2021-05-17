from typing import List

MOD = 1_000_000


def t(n: int) -> List[int]:
    # Conditions
    # (1, L, 1) where L contains no 2
    # (2, L, 2) where L contains no 2
    # (x, L ,x) where L contains no 2 and x > 2
    # (x, L, x) where L contains 2 and x > 0
    dp = [
        [0, 0, 0, 0],  # 1
        [1, 0, 0, 0],  # 2
    ]
    res = [0, 0, 1]
    for i in range(3, n + 1):
        ndp = [0] * 4
        ndp[3 if i == 4 else 0] = 1
        ndp[0] += dp[0][0] + dp[0][2]
        ndp[1] += dp[0][0]
        ndp[2] += dp[0][1] + dp[0][2]
        ndp[3] += dp[0][1] + dp[0][3] * 2
        for j in range(4):
            ndp[j] %= MOD
        dp.append(ndp)
        dp.pop(0)

        res.append((ndp[1] + ndp[3]) % MOD)

    return res


def test_t():
    assert t(6)[6] == 4
    assert t(42)[42] == 999923


def main():
    n = 2_000_000
    res = t(n)
    for i in range(43, n):
        if res[i] == 0:
            print(i)
            return


if __name__ == '__main__':
    main()
