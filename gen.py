from functools import partial
import random
import ints_pb2
import struct
import os.path
from google.protobuf.descriptor import FieldDescriptor

def _fill(p, name, bits=None):
  setattr(p, name, _rand(bits))

def _rand(bits):
  bits = random.randint(1, bits)
  return random.getrandbits(bits)

FILL_FUNC = {
  FieldDescriptor.TYPE_INT32: partial(_fill, bits=31),
  FieldDescriptor.TYPE_INT64: partial(_fill, bits=63),
  FieldDescriptor.TYPE_UINT32: partial(_fill, bits=32),
  FieldDescriptor.TYPE_UINT64: partial(_fill, bits=64),
}

def fillRandom(p):
  '''
  Fill proto by setting fields to random values, based on field type, optionality, etc.
  '''
  pDesc = p.DESCRIPTOR
  for fDesc in pDesc.fields:
    f = FILL_FUNC[fDesc.type]
    f(p, fDesc.name)

def main():
  _writeProtos("d/ints", ints_pb2.Ints1, 100)
  _writeProtos("d/ints", ints_pb2.Ints1, 1000)
  _writeProtos("d/ints", ints_pb2.Ints1, 10000)

def _writeProtos(path, protoF, n):
  p = protoF()
  with open(os.path.join(path, '%s.%d.pb' % (p.DESCRIPTOR.full_name, n)), 'wb+') as f:
    for i in xrange(n):
      p = protoF()
      fillRandom(p)
      buf = p.SerializeToString()
      l = len(buf)
      f.write(struct.pack('<I%ds' % l, l, buf))

if __name__ == '__main__':
  main()
