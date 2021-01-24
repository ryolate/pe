MOD = 1_000_000_007


def inv(a: int) -> int:
    return pow(a, MOD - 2, MOD)


inv9 = inv(9)


def S(k: int) -> int:
    l = k // 9
    k = k % 9
    res = -(9 * l + k + 54 * inv9) + (54 * inv9 + k * (k + 3) // 2) * pow(10, l, MOD)
    return (res % MOD + MOD) % MOD


def test_S():
    assert S(20) == 1074


def main():
    a, b = 0, 1
    res = 0
    for i in range(2, 91):
        a, b = b, a + b
        res += S(b)
    res = (res % MOD + MOD) % MOD
    print(res)


if __name__ == "__main__":
    main()
