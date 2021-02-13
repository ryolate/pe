import { Heap, F } from './425'

test('heap', () => {
    let h = new Heap((a: number, b) => { return a < b })
    for (const x of [3, 1, 4, 1, 5, 9]) {
        h.insert(x)
    }
    let got = []
    for (let i = 0; i < 6; i++) {
        got.push(h.delete_min())
    }
    expect(got).toStrictEqual([1, 1, 3, 4, 5, 9])
})

test('heap generic', () => {
    let h = new Heap<[number, number]>((a, b) => {
        if (a[0] != b[0])
            return a[0] < b[0]
        return a[1] < b[1]
    })
    h.insert([20, 2])
    h.insert([100, 3])
    h.insert([4, 4])
    h.insert([100, 2])
    let got = []
    for (let i = 0; i < 4; i++) {
        got.push(h.delete_min())
    }
    expect(got).toStrictEqual([
        [4, 4],
        [20, 2],
        [100, 2],
        [100, 3]
    ])
})

test('F', () => {
    expect(F(1000)).toBe(431)
    expect(F(10000)).toBe(78728)
})
