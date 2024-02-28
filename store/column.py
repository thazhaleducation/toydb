from store.datatype import Datatype

class Column:
  def __init__(self, position: int, name: str, datatype: Datatype, length: int=1):
    self.name=name
    self.position=position
    self.datatype=datatype
    self.length = length
  
  def bits_to_read(self) -> int:
    return self.datatype.length * self.length
  
