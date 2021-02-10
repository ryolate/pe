import math

MOD = 10 ** 9 + 7


def T(n: int, k: int) -> int:
    N = math.ceil(math.log2(n))
    NN = 1 << N

    isPrime = [1] * NN
    isPrime[0] = isPrime[1] = 0
    for i in range(NN):
        if isPrime[i] == 0:
            continue
        for j in range(2 * i, NN, i):
            isPrime[j] = 0
    sumPrime = isPrime.copy()
    for i in range(N):
        for j in range(NN):
            if j & 1 << i:
                sumPrime[j] += sumPrime[j ^ 1 << i]
    sumRes = [0] * NN
    for i in range(n + 1):
        sumRes[i] = pow(sumPrime[i], k, MOD)

    for i in range(N):
        for j in range(NN):
            if j & 1 << i:
                sumRes[j] -= sumRes[j ^ 1 << i]
                sumRes[j] %= MOD
    res = 0
    for i in range(n + 1):
        if isPrime[i]:
            res = (res + sumRes[i]) % MOD
    return (res % MOD + MOD) % MOD


def test_T():
    assert T(5, 2) == 5
    assert T(100, 3) == 3355
    assert T(1000, 10) == 2071632


def main():
    print(T(10 ** 6, 999983))


if __name__ == "__main__":
    main()
