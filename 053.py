def main():
    n = 100
    fact = [1] * (n+1)
    for i in range(n):
        fact[i+1] = (i+1)*fact[i]
    res = 0
    for i in range(1, n+1):
        for j in range(0, i+1):
            C = fact[i] / fact[j] / fact[i-j]
            if C > 1_000_000:
                res += 1
    print(res)


if __name__ == '__main__':
    main()
