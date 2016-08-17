from __transformers__ import matmul_pipe, ellipsis_partial


def test(x):
    return x @ range(...) @ map(lambda x: x + 1, ...) @ sum
