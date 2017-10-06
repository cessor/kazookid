class Substitute(object):

    '''
    Substitutes are can be used to provide or verify
    direct and indirect input and output of objects
    during testing.

    See: http://xunitpatterns.com/

    Test Spy
    ========

    Test Spies capture indirect output
    http://xunitpatterns.com/Test%20Spy.html

    # Check if a method was called

        from kazookid import Substitute

        def test_spy():
            engine = Substitute()
            game = Game(engine)
            game.run()
            assert_true(engine.render.was_called)

    # Check on parameters

        def test_spy():
            engine = Substitute()
            game = Game(engine)
            game.run()
            assert_true(engine.render.was_called_with(time))


    Test Stub
    =========

    Stubs feed indirect input into the System under Test
    http://xunitpatterns.com/Test%20Stub.html

    # To provide indirect input:

        substitute.value = 5

        substitute.method.returns(1)

        substitute.method.raises(Exception)
    '''

    def __init__(self):
        self._calls = {}
        self._config = {}
        self._iterator = Iterator()

    def __getattr__(self, name):
        if name == 'yields':
            return self._iterator

        config = self.__dict__['_config']
        call = Call(name=name, parent=self)
        config[name] = config.get(name, call)
        return config[name]

    def __iter__(self):
        return self._iterator.__iter__()


class Context(Substitute):

    def __enter__(self, *args, **kwargs):
        return self

    def __exit__(self, *args, **kwargs):
        pass


class Call(object):

    '''
    Intercepts a call or method on a substitute object
    '''

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.return_value = None
        self.exception = None

    def __call__(self, *args, **kwargs):
        if self.exception:
            raise self.exception()

        self.parent._calls[self.name] = (args, kwargs)
        try:
            return self.return_value[0]
        except:
            return None

    @property
    def args(self):
        args, kwargs = self.parent._calls.get(self.name, (None, None))
        if len(args) == 1:
            return args[0]
        return args

    def raises(self, exception):
        self.exception = exception

    def returns(self, *args, **kwargs):
        self.return_value = args

    @property
    def was_called(self):
        return self.name in self.parent._calls

    def was_called_with(self, *args):
        if len(args) == 1:
            args = args[0]
        return self.was_called and self.args == args


class Iterator(object):

    def __init__(self):
        self._items = []

    def __iter__(self):
        return self._items.__iter__()

    def __call__(self, items):
        self._items = items
