MOD = 1_001_001_011


def next_mask(x: int, n: int) -> int:
    b1, b2, b3 = x & 1, (x >> 1) & 1, (x >> 2) & 1
    return x >> 1 | (b1 & (b2 ^ b3)) << (n-1)


def dfs_tree(prev, is_core, i, mark, cache):
    key = ("dfs_tree", i, mark)
    if key in cache:
        return cache[key]

    res = 1
    for j in prev[i]:
        if is_core[j]:
            continue
        val = 0
        for n_mark in [True, False]:
            if mark and n_mark:
                continue
            val += dfs_tree(prev, is_core, j, n_mark, cache)
        res = (res * val) % MOD
    cache[key] = res
    return res


def dfs_core(next, prev, is_core, i, mark, r, r_mark, cache):
    key = ("dfs_core", i, mark, r, r_mark)
    if key in cache:
        return cache[key]

    res = dfs_tree(prev, is_core, i, mark, cache)
    if next[i] == r:
        return 0 if mark and r_mark else res

    val = 0
    for n_mark in [True, False]:
        if mark and n_mark:
            continue
        val += dfs_core(next, prev, is_core, next[i], n_mark, r, r_mark, cache)
    res = (res * val) % MOD
    cache[key] = res
    return res


def S(n: int) -> int:
    next = [next_mask(i, n) for i in range(1 << n)]
    prev = [[] for _ in range(1 << n)]
    for i in range(1 << n):
        prev[next[i]].append(i)

    next_doubling = next.copy()
    for _ in range(n):
        tmp = next_doubling.copy()
        for i in range(1 << n):
            tmp[i] = next_doubling[next_doubling[i]]
        next_doubling = tmp

    is_core = [False] * (1 << n)
    for i in range(1 << n):
        is_core[next_doubling[i]] = True

    res = 1

    cache = {}

    seen_core = set()
    for i in range(1 << n):
        if not is_core[i] or (i in seen_core):
            continue
        while i not in seen_core:
            seen_core.add(i)
            i = next[i]
        value = 0
        for mark in [True, False]:
            value += dfs_core(next, prev, is_core, i, mark, i, mark, cache)
        res = (res * value) % MOD
    return res


def test_S():
    assert S(3) == 35
    assert S(4) == 2118


def main():
    print(S(20))


if __name__ == "__main__":
    main()
