import sys

from typing import List
from multiprocessing import Pool
import z3


def solve(problem: List[str]) -> int:
    X = [[z3.Int(f"x{i}{j}") for j in range(9)] for i in range(9)]
    solver = z3.Solver()

    for i in range(9):
        for j in range(9):
            solver.add(1 <= X[i][j], X[i][j] <= 9)
    for i in range(9):
        solver.add(z3.Distinct(X[i]))
    for j in range(9):
        solver.add(z3.Distinct([X[i][j] for i in range(9)]))
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            solver.add(z3.Distinct(
                [X[i + d // 3][j + d % 3] for d in range(9)]))

    for i in range(9):
        for j in range(9):
            if problem[i+1][j] != '0':
                solver.add(X[i][j] == ord(problem[i+1][j]) - ord('0'))

    if solver.check() != z3.sat:
        print(f"{problem[0]} unsat")
        return 0
    return solver.model().evaluate(X[0][0] * 100 + X[0][1] * 10 + X[0][2]).as_long()


def main():
    ls = [x.strip() for x in sys.stdin.readlines()]
    with Pool(15) as p:
        answers = p.map(solve, (ls[i:i+10] for i in range(0, len(ls), 10)))
        print(sum(answers))


if __name__ == '__main__':
    main()
