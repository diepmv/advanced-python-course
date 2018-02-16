"""
class Widget:
    pass

name = 'Widget'
metaclass = type
bases = ()
kwargs = {}
namespace = metaclass.__prepare__(name, bases, **kwargs)
Widget = metaclass.__new__(metaclass, name, bases, namespace, **kwargs)
metaclass.__init__(Widget, name, bases, namspace, **kwargs)
"""

class TracingMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print("metaclass: {}".format(mcs))
        print("name: ".format(name))
        print("bases: ".format(bases))
        print("keyword arguments: {}".format(kwargs))
        namespace = super().__prepare__(name, bases)
        return namespace
    @classmethod
    def __new__(mcs, name, bases, namespace, **kwargs):
        print("print from new")
	print("mcs: {}".format(mcs))
	print("name: {}".format(name))
	print("bases: {}".format(bases))
	print("namespace: {}".format(namespace))
	num_entries = kwargs['num_entries']
	namespace.update({chr(i): i for i in range(ord('a'), ord('a')+num_entries)})
        cls = super().__new__(mcs, name, bases, namespace)
	print("cls: {}".format(cls))
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
	print("print from init")
	print("cls : {}".format(cls))
	print("name: {}".format(name))
	print("bases: {}".format(bases))
	print("namespace: {}".format(namespace))
	print("keyword argument: {}".format(kwarg))
	super().__init__(names, bases, namespace)

    def metamethod(cls):
	print("TracingMeta.metamethod(cls)")
	print("cls =", cls)
	print()

class Widget(metaclass=TracingMeta):
  def hello(self):
    pass
