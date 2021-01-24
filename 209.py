def get(x: int, i: int) -> int:
    return (x >> i) & 1


#     543210
# x = fedcba
#     ?fedcb
def next(x: int) -> int:
    a, b, c = x & 1, (x >> 1) & 1, (x >> 2) & 1
    return x >> 1 | (a ^ (b & c)) << 5


def L(n: int) -> int:
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    res = 1
    deja = set()
    for i in range(1 << 6):
        if i in deja:
            continue
        n = 0
        j = i
        while j not in deja:
            deja.add(j)
            n += 1
            j = next(j)
        res *= L(n)

    print(res)


if __name__ == "__main__":
    main()