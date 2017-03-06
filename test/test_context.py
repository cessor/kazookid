from nose.tools import *
from kazookid import Context


def test_context_manager():
    '''Context: How to create a Context'''
    assert_true(Context())

def test_can_enter_and_exit_a_context():
    '''Context: Can Enter a Context'''
    with Context() as context:
        assert_true(context)
        context.method()

    # Can still do the same tricks
    assert_true(context.method.was_called)
    assert_false(context.different_method.was_called)