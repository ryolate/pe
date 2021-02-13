let a = 1
let b = 1

let res = 0
while (b < 4_000_000) {
    if (b % 2 == 0) {
        res += b
    }
    [a, b] = [b, a + b]
}
console.log(res)
