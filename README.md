Kazookid
========

[![Build Status](https://travis-ci.org/cessor/kazookid.svg?branch=master)](https://travis-ci.org/cessor/kazookid)

This library allows you to create objects that impersonate other objects:

```
# pretend to be a pathlib.Path
path = pretend()

program = Program(path)
program.save('content')

assert_true(path.write_text.was_called_with('content'))
```

Where can I use that?
---------------------

In tests.

Objects play with other objects. This makes it hard to test objects in isolation, because when you create them, you need to create their friends as well. This library allows you to provide friends for your object to play with.

> So... like mocks?

Yes. Others call such objects mocks, stubs, dummies, spies, test doubles, or fakes. However, I find these terms unhelpful and confusing, which is why I try to avoid them.


How do I use it?
----------------

Take a look at the tests. The tests explain how substitutes behave and can be used as examples.

https://github.com/cessor/kazookid/blob/master/test/test_substitute.py

You always start with ```pretend```. Pretend creates a ```Substitute``` object. You can also create them directly. However if you know the kazookid, the pretend function might be more memorable.

```
from kazookid import pretend

# ...

path = pretend()
```

Then you configure what the substitute should do:

```
path.read_text.returns('content')
```

Then you pass the object to the actual component that you would like to test:

```
# Arrange
path = pretend()
path.read_text.returns('1 2 3 4')

# System under Test
# SquareNumbers implements an iterator.
square_numbers = SquareNumbers(read_from=path)

# Act
result = list(square_numbers)

# Assert
assert_equal(result, [1, 4, 9, 16])
```

Examples
--------

### Creating a Substitute

 - [How to create a Substitute](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L5)
 - [How to call a method on a substitute](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L31)
 - [How to provide data from a property](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L151)
 - [How to provide data from a method](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L135)
 - [How to provide data for iteration](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L203)
 - [How to raise exceptions](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L188)

### Verifying that a method was called

 - [How to intercept the arguments of a call](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L109)
 - [How to verify that a method was called](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L44)
 - [How to verify that a method was called several times](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L58)
 - [How to verify that a method was called with specific arguments](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L77)

### Implementation details

 - [Properties containing functions are methods](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L167)
 - [When a call had many arguments, they are returned as a tuple](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L122)
 - [When a method was called several times, all arguments are stored](https://github.com/cessor/kazookid/blob/master/test/test_substitute.py#L94)

There is also a substitute for context managers:

 - [How to create a Context](https://github.com/cessor/kazookid/blob/master/test/test_context.py#L5)


Trivia
------

Named after the kazookid: https://www.youtube.com/watch?v=D06m5ndmVsM
<!-- https://www.youtube.com/watch?v=g-sgw9bPV4A -->

This is a simplified implementation of my original framework, https://github.com/cessor/substitute, which was getting too complex.
