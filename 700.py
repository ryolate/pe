base = 1_504_170_715_041_707
mod = 4_503_599_627_370_517

th = 20_000_000


def main():
    ibase = pow(base, mod-2, mod)

    res = base
    min = base
    cur = base

    while min > th:
        cur += base
        if cur >= mod:
            cur -= mod
        if cur < min:
            min = cur
            res += cur

    ids = []
    for i in range(1, min):
        ids.append((i * ibase % (mod - 1), i))
    ids.sort()
    for (_, i) in ids:
        if i < min:
            min = i
            res += i
    print(res)


if __name__ == '__main__':
    main()
