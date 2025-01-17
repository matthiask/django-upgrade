import ast
import warnings
from typing import Union

from tokenize_rt import Offset


def ast_parse(contents_text: str) -> ast.Module:
    # intentionally ignore warnings, we can't do anything about them
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return ast.parse(contents_text.encode())


def ast_start_offset(node: Union[ast.expr, ast.keyword, ast.stmt]) -> Offset:
    return Offset(node.lineno, node.col_offset)


# def ast_end_offset(node: Union[ast.expr, ast.keyword, ast.stmt]) -> Offset:
#     return Offset(node.end_lineno, node.end_col_offset)
