# -*- coding = utf-8 -*-
# pip install recordclass


import sys

class Shape:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class ShapeSlot:

    __slots__ = 'x', 'y', 'z'

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z   

ex_dict = {'x': 1, 'y': 2, 'z': 3}
print('dict: {} byte'.format(sys.getsizeof(ex_dict)))

ex = Shape(1, 2, 3)
print('ex  : {} byte'.format(sys.getsizeof(ex) + sys.getsizeof(ex.__dict__)))

ex_slot = ShapeSlot(1, 2, 3)
print('ex_slot: {} byte'.format(sys.getsizeof(ex_slot)))

from collections import namedtuple

ShapeNamedTuple = namedtuple('ShapeNamedTuple', ['x', 'y', 'z'])
ex_namedtuple = ShapeNamedTuple(1, 2, 3)
print('ex_namedtuple: {} byte'.format( sys.getsizeof(ex_namedtuple)))

from recordclass import recordclass
ShapeRecord = recordclass('ShapeRecord', ('x', 'y', 'z'))
ex_record = ShapeRecord(1, 2, 3)
print('ex_record: {} byte'.format( sys.getsizeof(ex_record)))


from recordclass import make_dataclass
ShapeMake = make_dataclass('ShapeMake', ('x', 'y', 'z'))
ex_make = ShapeMake(1, 2, 3)
print('ex_make: {} byte'.format( sys.getsizeof(ex_make)))
