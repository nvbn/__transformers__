import ast
from __transformers__.ellipsis_partial import transformer


def test_transformer():
    code = 'result = map(lambda x: x + 1, ...)(range(5))'
    tree = ast.parse(code)
    tree = transformer.visit(tree)
    code = compile(tree, '<string>', 'exec')
    exec(code)
    assert list(locals()['result']) == [1, 2, 3, 4, 5]
