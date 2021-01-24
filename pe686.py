import math


def p(L: int, n: int) -> int:
    l = 0
    while True:
        l += 1
        m = math.ceil(math.log2(L) + l * math.log2(10))
        m2 = math.floor(math.log2(L + 1) + l * math.log2(10))
        if m == m2:
            n -= 1
            if n == 0:
                return m2


def test_p():
    assert p(12, 1) == 7
    assert p(12, 2) == 80
    assert p(123, 45) == 12710


def main():
    print(p(123, 678910))


if __name__ == "__main__":
    main()
