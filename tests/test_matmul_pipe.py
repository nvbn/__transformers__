import ast
from __transformers__.matmul_pipe import transformer


def test_transformer():
    code = 'result = range(10) @ sum'
    tree = ast.parse(code)
    tree = transformer.visit(tree)
    code = compile(tree, '<string>', 'exec')
    exec(code)
    assert locals()['result'] == 45
