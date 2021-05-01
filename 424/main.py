from z3 import Solver, Int, Ints, Or, Distinct, And, sat, ModelRef
from typing import List, Union, Iterator, NewType
import sys


class Wall:
    def __init__(self, h: str, v: str):
        self.h = h
        self.v = v


Empty = NewType('Empty', str)
Square = Union[Empty, Wall]
Board = List[List[Square]]

isa = isinstance


def parse_square(it: Iterator[str]) -> Square:
    c = next(it)
    if c == 'X':
        return Wall("", "")
    if c == 'O':
        return Empty("")
    if c != '(':
        return Empty(c)
    s = ""
    for c in it:
        if c == ')':
            break
        s = s + c
    [h, v] = ["", ""]
    for hint in s.split(","):
        if hint[0] == 'h':
            h = hint[1:]
        else:
            v = hint[1:]
    return Wall(h, v)


def parse_board(it: Iterator[str]) -> Board:
    n = int(next(it))
    board: Board = []
    for i in range(n):
        board.append([])
        for _ in range(n):
            next(it)  # ,
            board[i].append(parse_square(it))
    return board


def solve(problem: str) -> int:
    board = parse_board(iter(problem))
    n = len(board)

    solver = Solver()

    def num(c): return ord(c) - ord('A')

    # Set up parameters
    L = Ints('A B C D E F G H I J')
    X: List[List[Int]] = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b = board[i][j]
            if isa(b, Wall):
                continue
            if b == "":
                X[i][j] = Int(f"x{i}{j}")
            else:
                X[i][j] = L[num(b)]

    # Add constraints
    solver.add(Distinct(L))
    solver.add([And(0 <= l, l <= 9) for l in L])
    for i in range(n):
        for j in range(n):
            if X[i][j] is not None:
                solver.add(And(1 <= X[i][j], X[i][j] <= 9))
    for i in range(n):
        for j in range(n):
            b = board[i][j]
            if not isinstance(b, Wall):
                continue
            for d in range(2):
                s, di, dj = (b.h, 0, 1) if d == 0 else (b.v, 1, 0)
                if not s:
                    continue
                solver.add(L[num(s[0])] != 0)  # no leading zeros
                hint = 0
                for c in s:
                    hint *= 10
                    hint += L[num(c)]
                targets = []
                for k in range(1, n):
                    ni = i + di * k
                    nj = j + dj * k
                    if ni >= n or nj >= n or (X[ni][nj] is None):
                        break
                    targets.append(X[ni][nj])

                solver.add(hint == sum(targets))
                solver.add(Distinct(targets))

    if solver.check() != sat:
        print("failed to solve")
        return 0

    answer_keys = []
    for _ in range(100):
        m = solver.model()

        answer_keys.append(answer_key(m, L))

        add_constraint(solver, m)
        if solver.check() != sat:
            break

    if len(answer_keys) > 1:
        print(
            f"multiple solutions: {problem} -> {answer_keys}")

    return answer_keys[-1]


def answer_key(m: ModelRef, L) -> int:
    res = 0
    for l in L:
        res *= 10
        res += m.evaluate(l).as_long()
    return res


def add_constraint(s: Solver, model: ModelRef):
    block = []
    for d in model:
        # create a constant from declaration
        block.append(d() != model[d])
    s.add(Or(block))


def main():
    from multiprocessing import Pool
    with Pool(15) as p:
        answers = p.map(solve, sys.stdin)
        print(sum(answers))


if __name__ == '__main__':
    main()
