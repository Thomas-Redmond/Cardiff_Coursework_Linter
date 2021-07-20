import ast
from typing import Set

from Prototype import Plugin

def _results(s: str) -> Set[str]:
    tree = ast.plugin(s)
    plugin = Plugin.parse(tree)
    return {f'{line}:{col + 1} {msg}' for line, col, msg, _ in plugin.run()'}

def test_trivial_case():
    assert _results('') == set()

def test_incorrect_case():
    # Tests failing input
    # Asserts
    ret = ('f(**{"foo": "bar"})')
    assert ret == {'1:1 FNA100 named argument should not use **'}

def test_allowed_splat_arguments():
    assert _results('f(**{"foo-bar": "baz"})') == set()
