export class Heap<T> { // min heap

    // left: 2i+1
    // right: 2i+2
    // parent: (i-1)/2
    //
    // It must hold that parent <= children
    a: Array<T>
    sz: number
    lt: (x: T, y: T) => boolean
    constructor(lt: (x: T, y: T) => boolean) {
        this.a = new Array()
        this.sz = 0
        this.lt = lt
    }

    delete_min(): T {
        if (this.sz == 0) {
            throw new Error("delete_min: empty")
        }
        let res = this.a[0]
        this.sz--
        this.a[0] = this.a.pop() as T

        for (let p = 0; p < this.sz;) {
            let [l, r] = [p * 2 + 1, p * 2 + 2]
            let minID = p
            if (l < this.sz && this.lt(this.a[l], this.a[minID])) {
                minID = l
            }
            if (r < this.sz && this.lt(this.a[r], this.a[minID])) {
                minID = r
            }
            if (minID == p) {
                break
            }
            [this.a[minID], this.a[p]] = [this.a[p], this.a[minID]]
            p = minID
        }
        return res
    }

    insert(t: T) {
        this.a[this.sz] = t; // automatially expands

        for (let c = this.sz; c > 0;) {
            let p = (c - 1) >> 1
            if (this.lt(this.a[p], this.a[c])) { // ok
                break
            }
            // swap
            [this.a[p], this.a[c]] = [this.a[c], this.a[p]]
            c = p
        }
        this.sz++
    }
}

export function F(n: number): number {
    let isPrime = [];
    isPrime[1] = false;
    for (let i = 2; i <= n; i++) {
        if (isPrime[i] !== undefined) {
            continue
        }
        isPrime[i] = true
        for (let j = i * 2; j <= n; j += i) {
            isPrime[j] = false
        }
    }

    let q = new Heap<[number, number]>((a, b) => {
        if (a[0] != b[0]) return a[0] < b[0]
        return a[1] < b[1]
    })
    q.insert([2, 2]) // smallest intermediate, value

    let res = 0
    let seen = []
    while (q.sz > 0) {
        const [i, v] = q.delete_min()
        if (seen[v]) {
            continue
        }
        if (i <= v) res -= i
        seen[v] = true

        for (let p = 1; p <= v * 10; p *= 10) {
            for (let j = 0; j < 10; j++) {
                if (j == 0 && p * 10 > v) continue

                const nv = v - Math.floor(v / p) % 10 * p + j * p
                if (!isPrime[nv] || seen[nv]) {
                    continue
                }
                q.insert([Math.max(i, nv), nv])
            }
        }
    }
    for (let i = 0; i <= n; i++) {
        if (isPrime[i]) res += i
    }
    return res
}

if (require.main == module) {
    console.log(F(10_000_000))
}
