from scipy import sparse
from scipy.sparse import linalg
import math
import decimal


def C(h: int, w: int) -> float:
    L = sparse.lil_matrix((h * w - 1, h * w - 1))
    for i in range(h):
        for j in range(w):
            if i + j == 0:
                continue
            for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 > ni or ni >= h or 0 > nj or nj >= w:
                    continue
                L[i * w + j - 1, i * w + j - 1] += 1
                if ni + nj > 0:
                    L[i * w + j - 1, ni * w + nj - 1] -= 1

    LU = linalg.splu(L.tocsc())
    logd = 0
    for d in LU.U.diagonal():
        logd += math.log(d)
    return decimal.Decimal(logd).exp()


def test_C():
    assert round(C(2, 2)) == 4
    assert round(C(3, 4)) == 2415
    assert f"{C(9, 12):.4e}" == "2.5720e+46"


def main():
    print(f"{C(100, 500):.4e}".replace("+", ""))


if __name__ == '__main__':
    main()
