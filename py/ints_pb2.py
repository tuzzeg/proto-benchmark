# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: d/ints/ints.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='d/ints/ints.proto',
  package='ints',
  serialized_pb=_b('\n\x11\x64/ints/ints.proto\x12\x04ints\"g\n\x05Ints1\x12\n\n\x02i1\x18\x01 \x02(\x05\x12\n\n\x02i2\x18\x02 \x02(\x03\x12\n\n\x02i3\x18\x03 \x02(\r\x12\n\n\x02i4\x18\x04 \x02(\x04\x12\n\n\x02i5\x18\x05 \x01(\x05\x12\n\n\x02i6\x18\x06 \x01(\x03\x12\n\n\x02i7\x18\x07 \x01(\r\x12\n\n\x02i8\x18\x08 \x01(\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INTS1 = _descriptor.Descriptor(
  name='Ints1',
  full_name='ints.Ints1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='i1', full_name='ints.Ints1.i1', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i2', full_name='ints.Ints1.i2', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i3', full_name='ints.Ints1.i3', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i4', full_name='ints.Ints1.i4', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i5', full_name='ints.Ints1.i5', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i6', full_name='ints.Ints1.i6', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i7', full_name='ints.Ints1.i7', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='i8', full_name='ints.Ints1.i8', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['Ints1'] = _INTS1

Ints1 = _reflection.GeneratedProtocolMessageType('Ints1', (_message.Message,), dict(
  DESCRIPTOR = _INTS1,
  __module__ = 'd.ints.ints_pb2'
  # @@protoc_insertion_point(class_scope:ints.Ints1)
  ))
_sym_db.RegisterMessage(Ints1)


# @@protoc_insertion_point(module_scope)
