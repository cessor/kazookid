Kazookid
========

This library allows you to create objects that impersonate other objects:

```
# Impersonating a pathlib.Path
path = Substitute()

program = Program(path)
program.save('content')

assert_true(path.write_text.was_called_with(content))
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

You always start with a substitute:

```
from kazookid import Substitute

# ...

path = Substitute()
```

Then, you configure what the substitute should do:

```
path.read_text.returns('content')
```

Then you pass the object to the actual component, that you would like to test:

```
# Arrange
path = Substitute()
path.read_text.returns('1 2 3 4')

# System under Test
# Lines implements an iterator.
square_numbers = SquareNumbers(read_from=path)

# Act
assert_equal(list(square_numbers), [1, 4, 9, 16])
```


Trivia
------

Named after the kazookid: https://www.youtube.com/watch?v=D06m5ndmVsM
<!-- https://www.youtube.com/watch?v=g-sgw9bPV4A -->


