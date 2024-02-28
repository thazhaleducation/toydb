from enum import Enum


class Datatype():
  def __init__(self, name, length):
    self.name = name
    self.length = length

  def name(self):
    return self.name
  
  def length(self):
    return self.length
  
INT = Datatype("INT", 4)
CHAR = Datatype("CHAR", 1)

def get_datatype(typeStr):
  if typeStr.upper() == "INT":
    return INT
  elif typeStr.upper() == "CHAR":
    return CHAR
  else:
    raise Exception("Exception unsupported datatype" + typeStr)
  