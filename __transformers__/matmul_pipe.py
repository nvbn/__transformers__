import ast


class MatMulPipeTransformer(ast.NodeTransformer):
    def _replace_with_call(self, node):
        """Call right part of operation with left part as an argument."""
        return ast.Call(func=node.right, args=[node.left], keywords=[])

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.MatMult):
            node = self._replace_with_call(node)
            node = ast.fix_missing_locations(node)

        return self.generic_visit(node)


transformer = MatMulPipeTransformer()
