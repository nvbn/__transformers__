import ast


class EllipsisPartialTransformer(ast.NodeTransformer):
    def __init__(self):
        self._counter = 0

    def _get_arg_name(self):
        """Return unique argument name for lambda."""
        try:
            return '__ellipsis_partial_arg_{}'.format(self._counter)
        finally:
            self._counter += 1

    def _is_ellipsis(self, arg):
        return isinstance(arg, ast.Ellipsis)

    def _replace_argument(self, node, arg_name):
        """Replace ellipsis with argument."""
        replacement = ast.Name(id=arg_name,
                               ctx=ast.Load())
        node.args = [replacement if self._is_ellipsis(arg) else arg
                     for arg in node.args]
        return node

    def _wrap_in_lambda(self, node):
        """Wrap call in lambda and replace ellipsis with argument."""
        arg_name = self._get_arg_name()
        node = self._replace_argument(node, arg_name)
        return ast.Lambda(
            args=ast.arguments(args=[ast.arg(arg=arg_name, annotation=None)],
                               vararg=None, kwonlyargs=[], kw_defaults=[],
                               kwarg=None, defaults=[]),
            body=node)

    def visit_Call(self, node):
        if any(self._is_ellipsis(arg) for arg in node.args):
            node = self._wrap_in_lambda(node)
            node = ast.fix_missing_locations(node)

        return self.generic_visit(node)


transformer = EllipsisPartialTransformer()
