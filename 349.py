def main():
    STEP = 10 ** 18

    grid = [[False] * 1000 for _ in range(1000)]
    x, y = 500, 500
    n = 12000
    d = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    counts = [0]
    for _ in range(1, n):
        count = counts[-1]
        if grid[x][y]:
            grid[x][y] = False
            d = (d + 3) % 4
            count -= 1
        else:
            grid[x][y] = True
            count += 1
            d = (d + 1) % 4
        counts.append(count)

        x += dx[d]
        y += dy[d]

    for per in range(1, 1000):
        ok = True
        d = counts[10000 + per] - counts[10000]
        for i in range(10000, n - per):
            if counts[i + per] - counts[i] != d:
                ok = False
                break
        if not ok:
            continue

        print(counts[10000 + (STEP - 10000) %
              per] + d * ((STEP - 10000) // per))

        return


if __name__ == '__main__':
    main()
