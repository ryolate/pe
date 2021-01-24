import numpy as np

MOD = 10 ** 9 + 7


def F(d: int) -> int:
    dp = np.zeros((3, 3, 3, 3), int)  # 0,1,2,sum
    dp[0][0][0][0] = 1
    for l in range(d):
        ndp = np.zeros((3, 3, 3, 3), int)
        for i0 in range(3):
            for i1 in range(3):
                for i2 in range(3):
                    for j in range(3):
                        if dp[i0][i1][i2][j] == 0:
                            continue
                        b = 1 if l == 0 else 0
                        for k in range(b, 10):
                            ni = [0, 0, 0]
                            ni[k % 3] = (i0 + 1) % 3
                            ni[(k + 1) % 3] = i1
                            ni[(k + 2) % 3] = i2
                            nj = (j + ni[0]) % 3
                            ndp[ni[0]][ni[1]][ni[2]][nj] += dp[i0][i1][i2][j]
                            ndp[ni[0]][ni[1]][ni[2]][nj] %= MOD
        dp = ndp
    res = 0
    for i0 in range(3):
        for i1 in range(3):
            for i2 in range(3):
                res = (res + dp[i0][i1][i2][0]) % MOD
    return res


def test_F():
    assert F(1) == 6
    assert F(2) == 30
    assert F(6) == 290898


def main():
    print(F(10 ** 5))


if __name__ == "__main__":
    main()