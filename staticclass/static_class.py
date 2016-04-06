class StaticMetaClass(type):
    def __new__(cls, name, parents, dct):
        for attr_name, item in dct.items():
            if StaticMetaClass._can_be_static(attr_name, item):
                dct[attr_name] = staticmethod(item)

        return super(StaticMetaClass, cls).__new__(cls, name, parents, dct)

    @staticmethod
    def _can_be_static(attr_name, attr):
        is_function = hasattr(attr, '__call__')
        is_protected = attr_name.startswith('__') or getattr(attr, '__notstatic__', False)
        return is_function and not is_protected


class StaticClass(object):
    __metaclass__ = StaticMetaClass
