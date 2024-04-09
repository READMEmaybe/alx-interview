"""Pascal's triangle"""

def pascal_triangle(n):
    """Return a list of lists representing the Pascal's triangle of n rows."""
    trngl = [[1]]
    for _ in range(1, n):
        row = [1] + [trngl[-1][i] + trngl[-1][i+1] for i in range(len(trngl[-1]) - 1)] + [1]
        trngl.append(row)
    return trngl
