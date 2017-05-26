import struct


class StructField:
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


# class Structure:
#     def __init__(self, bytedata):
#         self._buffer = memoryview(bytedata)


# class PolyHeader(Structure):
#     file_code = StructField('<i', 0)
#     min_x = StructField('<d', 4)
#     min_y = StructField('<d', 12)
#     max_x = StructField('<d', 20)
#     max_y = StructField('<d', 28)
#     num_polys = StructField('<i', 36)

# f = open('polys', 'rb')
# phead = PolyHeader(f.read(40))
# print(phead.file_code == 0x1234)
# print(phead.min_x, phead.min_y, phead.max_x, phead.max_y)


class StructureMeta(type):
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<','>','!','@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]


f = open('polys', 'rb')
phead = PolyHeader.from_file(f)
print(phead.file_code == 0x1234)
print(phead.min_x, phead.min_y, phead.max_x, phead.max_y)


class NestedStruct:
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            data = instance._buffer[
                self.offset: self.offset+self.struct_type.struct_size
            ]
            result = self.struct_type(data)
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    ''' Metaclass that automatically creates StructField description'''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith('<', '>', '!', '@'):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)