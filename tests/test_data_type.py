from store import datatype
import pytest

def test_datatype_returns_int():
  assert datatype.get_datatype("INT") == datatype.INT
  assert datatype.get_datatype("int") == datatype.INT

def test_datatype_returns_char():
  assert datatype.get_datatype("CHAR") == datatype.CHAR
  assert datatype.get_datatype("char") == datatype.CHAR

def test_datatype_returns_no_of_bits():
  assert datatype.INT.no_of_bits() == 32
  assert datatype.CHAR.no_of_bits() == 8

def test_datatype_raise_exception_for_unknown_datatype():
  with pytest.raises(Exception) as e:
    datatype.get_datatype("INTEGER")
  assert 'Exception unsupported datatypeINTEGER' == str(e.value)