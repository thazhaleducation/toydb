from store import data_type
import pytest

def test_datatype_returns_int():
  assert data_type.get_datatype("INT") == data_type.INT
  assert data_type.get_datatype("int") == data_type.INT

def test_datatype_returns_char():
  assert data_type.get_datatype("CHAR") == data_type.CHAR
  assert data_type.get_datatype("char") == data_type.CHAR

def test_datatype_raise_exception_for_unknown_datatype():
  with pytest.raises(Exception) as e:
    data_type.get_datatype("INTEGER")
  assert 'Exception unsupported datatypeINTEGER' == str(e.value)