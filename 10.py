test_list = 'abcde'
find_position = test_list.find('c')
pass


from array import array
import reprlib
import math
from functools import reduce
import operator
import itertools
import numbers

class Vector():
    typecode = "d"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    # def __eq__(self, other):
    #     return tuple(self) == tuple(other)

    # def __eq__(self, other):
    #     if len(self) != len(other):
    #         return False
    #     for a, b in zip(self, other):
    #         if a != b:
    #             return False
    #     return True
    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other) and all(a == b for a, b in zip(self, other)))
        else:
            return NotImplemented

    def __hash__(self):
#        hashes = (hash(x) for x in self._components)   # the improving method is as follows
        hashes = map(hash, self._components)
        return reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self._components))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

#    def __getitem__(self, item):
#        return self._components[item]

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, int):
            return self._components[item]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls = cls))

    short_names = 'xyzt'

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.short_names.find(item)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, item))

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.short_names:
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__,attr_name=key)
                raise AttributeError(msg)
        super().__setattr__(key, value)

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return self

    #if a.__add__(b) returns NotImplemented, then try b.__radd__(a)
    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(x + y for x, y in pairs)
        except TypeError:
            raise NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vector(x * other for x in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other


# a = Vector([1, 2, 3, 4, 5, 6, 7, 8])
#
# b = Vector([1, 2, 3, 4, 5])
#
# for x in a:
#     c = math.pow(x,2)
# c = abs(a) + abs(b)
# a == b
# a[2::2]
# lenght_a = len(a)
# slice_a = a[1:4]
# a.t
#a.t = 2IndentationError: unindent does not match any outer indentation level

a = Vector(list(range(1, 5)))
b = Vector(list(range(23, 27)))
c = a + b
#a and b is iterable
for x, y in zip(a,b):
    print(x, y)


pass



