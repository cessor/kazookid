from nose.tools import *
from kazookid import Substitute, pretend


def test_substitute():
    '''Substitute: How to create a Substitute'''

    # System under Test
    substitute = Substitute()


def test_pretend():
    '''Substitute: The kazookid likes to play pretend'''
    # see note.md

    # System under Test
    substitute = pretend()
    assert_true(isinstance(substitute, Substitute))


def test_substitute_nothing_happened():
    '''Substitute: New substitutes do nothing'''

    # System under Test
    substitute = Substitute()

    # Assert
    assert_false(substitute.method.was_called)


def test_call_method_returns_none():
    '''Substitute: How to call a method on a substitute'''

    # System under Test
    substitute = Substitute()

    # Act: Run
    data = substitute.method()

    # Assert
    assert_equal(data, None)


def test_call_method_on_substitute():
    '''Substitute: How to verify that a method was called'''

    # System under Test
    substitute = Substitute()

    # Act: Run
    substitute.method()

    # Assert
    assert_true(substitute.method.was_called)
    assert_false(substitute.other_method.was_called)


def test_calls_are_counted():
    '''Substitute: How to verify that a method was called several times'''

    # System under Test
    substitute = Substitute()

    # Arrange
    substitute.method()
    assert_true(substitute.method.was_called)
    assert_false(substitute.method.was_called_times(2))

    # Act: Run
    substitute.method()

    # Assert
    assert_true(substitute.method.was_called)
    assert_true(substitute.method.was_called_times(2))


def test_call_intercepts_asserts_arguments():
    '''Substitute: How to verify that a method was called with specific arguments'''

    # System under Test
    substitute = Substitute()

    # Act: Configure
    substitute.method.returns(1)

    # Act: Run
    data = substitute.method('hello')

    # Assert
    assert_true(substitute.method.was_called_with('hello'))
    assert_false(substitute.method.was_called_with('bye'))


def test_call_intercepts_several_arguments():
    '''Substitute: When a method was called several times, all arguments are stored'''

    # System under Test
    substitute = Substitute()

    # Act: Run
    substitute.method('hello')
    substitute.method('bye')

    # Assert
    assert_true(substitute.method.was_called_with('hello'))
    assert_true(substitute.method.was_called_with('bye'))


def test_call_intercepts_single_argument():
    '''Substitute: How to intercept the arguments of a call'''

    # System under Test
    substitute = Substitute()

    # Act: Run
    data = substitute.method('hello')

    # Assert
    assert_equal(substitute.method.args, 'hello')


def test_call_intercepts_many_arguments():
    '''Substitute: When a call had many arguments, they are returned as a tuple'''

    # System under Test
    substitute = Substitute()

    # Act: Run
    data = substitute.method('hello', 1, 2, 3)

    # Assert
    assert_equal(substitute.method.args, ('hello', 1, 2, 3))


def test_call_method_can_return_data():
    '''Substitute: How to provide data from a method'''

    # System under Test
    substitute = Substitute()

    # Act: Configure
    substitute.method.returns(1)

    # Act: Run
    data = substitute.method()

    # Assert
    assert_equal(data, 1)


def test_set_substitute_property():
    '''Substitute: How to provide data from a property'''

    # System under Test
    substitute = Substitute()

    # Act: Configure
    substitute.name = 'Johannes'

    # Act: Run
    name = substitute.name

    # Assert
    assert_equal(name, 'Johannes')


def test_set_substitute_method():
    '''Substitute: Properties containing functions are methods'''

    # System under Test
    substitute = Substitute()

    # Act: Configure
    substitute.name = lambda: 1

    # Act: Run
    name = substitute.name()

    # Assert
    assert_equal(name, 1)


class Apology(Exception):
    pass


@raises(Apology)
def test_call_method_can_raise_an_exception():
    '''Substitute: How to raise exceptions'''

    # System under Test
    substitute = Substitute()

    # Act: Configure
    substitute.method.raises(Apology)

    # Act: Run
    substitute.method()

    # Assert: @raises


def test_yields():
    '''Substitute: How to provide data for iteration'''

    # System under Test
    substitute = Substitute()

    # Act: Configure
    substitute.yields(['a', 'b', 'c'])

    # Act: Run
    result = list(substitute)

    # Assert
    assert_equal(result, ['a', 'b', 'c'])
