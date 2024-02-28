class Datatype():
  def __init__(self, name: str, length: int):
    self.name = name
    self.length = length

  def name(self) -> str:
    return self.name
  
  def no_of_bits(self) -> str:
    return self.length

INT = Datatype("INT", 32)
CHAR = Datatype("CHAR", 8)

def get_datatype(typeStr: str) -> Datatype:
  if typeStr.upper() == "INT":
    return INT
  elif typeStr.upper() == "CHAR":
    return CHAR
  else:
    raise Exception("Exception unsupported datatype" + typeStr)
  