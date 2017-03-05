from nose.tools import *
from kazoo import Substitute


def test_substitute():
    '''Substitute: How to create a Substitute'''
    substitute = Substitute()
    assert_false(substitute.method.was_called)


def test_call_method_returns_none():
    '''Substitute: How to call a method on a substitute'''
    substitute = Substitute()
    data = substitute.method()
    assert_equal(data, None)


def test_call_method_on_substitute():
    '''Substitute: How to verify that a method was called'''
    substitute = Substitute()
    substitute.method()
    assert_true(substitute.method.was_called)
    assert_false(substitute.other_method.was_called)


def test_call_intercepts_asserts_arguments():
    '''Substitute: How to verify that a method was called with specific arguments'''
    substitute = Substitute()
    substitute.method.returns(1)
    data = substitute.method('hello')
    assert_true(substitute.method.was_called_with('hello'))
    assert_false(substitute.method.was_called_with('bye'))


def test_call_intercepts_single_argument():
    '''Substitute: How to intercept the arguments of a call'''
    substitute = Substitute()
    data = substitute.method('hello')
    assert_equal(substitute.method.args, 'hello')


def test_call_intercepts_many_arguments():
    '''Substitute: If a call had many aruments, they are returned as a tuple'''
    substitute = Substitute()
    data = substitute.method('hello', 1, 2, 3)
    assert_equal(substitute.method.args, ('hello', 1, 2, 3))


def test_call_method_can_return_data():
    '''Substitute: How to provide data from a method'''
    substitute = Substitute()
    substitute.method.returns(1)

    data = substitute.method()
    assert_equal(data, 1)


def test_set_substitute_property():
    '''Substitute: How to provide data from a property'''
    substitute = Substitute()
    substitute.name = 'Johannes'
    assert_equal(substitute.name, 'Johannes')


def test_set_substitute_method():
    '''Substitute: Properties containing functions behave as such'''
    substitute = Substitute()
    substitute.name = lambda: 1
    assert_equal(substitute.name(), 1)


class Apology(Exception):
    pass

@raises(Apology)
def test_call_method_can_raise_an_exception():
    '''Substitute: How to raise exceptions'''
    substitute = Substitute()
    substitute.method.raises(Apology)
    substitute.method()
