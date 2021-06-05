import functools

class Proxy:
    def __init__(self, cls, obj) -> None:
        self.cls = cls
        self.obj = obj

    def __getattr__(self, attr):
        attr = getattr(self.cls, attr)
        if callable(attr):
            return functools.partial(attr, self.obj)
        return attr

def _super(cls, obj):
    mro = type(obj).mro()
    super_cls = mro[mro.index(cls) + 1]
    return Proxy(super_cls, obj)

class Base:
    def f(self):
        print('Base')


class A(Base):
    def f(self):
        print('A', end=', ')        
        _super(A, self).f()


class B(Base):
    def f(self):
        print('B', end=', ')
        _super(B, self).f()

class C(A, B):
    pass


C().f()
