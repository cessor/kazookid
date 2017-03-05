
class Substitute(object):

    '''
    Substitutes are can be used to provide or verify
    direct and indirect input and output of classes.

    # Test Spy:

    def test_spy():
        engine = Substitute()
        game = Game(engine)
        assert_true(engine.render.was_called)


    def test_spy():
        engine = Substitute()
        game = Game(engine)
        assert_true(engine.render.was_called_with(time))

    substitute.method.returns(1)

    '''

    def __init__(self):
        self._calls = {}
        self._config = {}

    def __getattr__(self, name):
        config = self.__dict__['_config']
        call = Call(name=name, parent=self)
        config[name] = config.get(name, call)
        return config[name]


class Call(object):

    '''Intercepts a call or method on a substitute object
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
