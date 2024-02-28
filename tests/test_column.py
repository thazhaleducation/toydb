from store.column import Column
from store.datatype import INT, CHAR

# add some_tests for column

def test_bits_to_read():
  assert Column(1, "id", INT).bits_to_read() == 32
  assert Column(1, "id", CHAR, 10).bits_to_read() == 80