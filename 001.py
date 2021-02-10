def f(n: int) -> int:
    res = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


def test_f():
    assert f(10) == 23


def main():
    print(f(1000))


if __name__ == '__main__':
    main()
