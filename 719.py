def possible(m: int, k: int) -> bool:
    if m == k:
        return True
    if m == 0 or k < 0 or k > m:
        return False
    p = 10
    while p < m:
        if possible(m // p, k - m % p):
            return True
        p *= 10
    return False


def T(n: int) -> int:
    res = 0
    for i in range(2, n):
        if i % (10**5) == 0:
            print('.')
        if i*i > n:
            return res
        m = i*i
        if possible(m, i):
            res += m
    return res


def test_T():
    assert T(10 ** 4) == 41333


def main():
    print(T(10 ** 12))


if __name__ == '__main__':
    main()
