import json

def dictionarize(byte_seq, encoding):
  return json.loads(byte_seq.decode(encoding))