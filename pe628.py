MOD = 1_008_691_207


def f(n: int) -> int:
    res = 1
    fact = 1
    for i in range(n):
        res -= (3 + i - n) * fact % MOD
        fact = fact * (i + 1) % MOD
        if i % 1000000 == 0:
            print("%.02f %% done" % (i / n * 100))
    res += fact
    return (res % MOD + MOD) % MOD


def test_f():
    assert f(5) == 70


def main():
    print(f(10 ** 8))


if __name__ == "__main__":
    main()
