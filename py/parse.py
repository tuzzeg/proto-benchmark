import ints_pb2 as pb
import struct
import timeit
import json
import argparse

def _read(f, fmt):
  l = struct.calcsize(fmt)
  buf = f.read(l)
  if not buf:
    return None
  v, = struct.unpack(fmt, buf)
  return v

def load(fileName):
  raw_protos = list()

  with open(fileName, 'rb') as f:
    while True:
      size = _read(f, '<I')
      if not size:
        break
      buf = _read(f, '%ds' % size)
      if not buf:
        break
      raw_protos.append(buf)

  return raw_protos

def parseAll(raw_protos):
  for buf in raw_protos:
    proto = pb.Ints1()
    proto.ParseFromString(buf)

if __name__ == '__main__':
  p = argparse.ArgumentParser()
  p.add_argument('--count', type=int, default=100)
  p.add_argument('--file', type=str)
  args = p.parse_args()

  repeats = args.count
  fileName = args.file

  from timeit import Timer
  t = timeit.Timer(stmt='parseAll(raw_protos)', setup='from __main__ import load, parseAll; raw_protos=load("%s")' % fileName)
  secs = t.timeit(number=repeats)

  print json.dumps({
    "library": "python-protobuf",
    "file": fileName,
    "count": repeats,
    "time-millis": int(secs*1000)
  })
