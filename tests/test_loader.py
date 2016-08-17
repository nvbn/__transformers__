from __transformers__.loader import setup


def test():
    setup()
    from .module_for_test import test

    assert test(10) == 55
