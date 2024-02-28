from store.table import Table
from store.context import Context
from store.column import Column
from store.datatype import INT, CHAR
from store.storage import create_schema
import pytest
import os
import shutil

@pytest.fixture
def setup():
  # create db
  create_schema("db1")
  context = Context()
  yield {
    "data": {
      "db": "db1",
      "name": "product",
      "columns": [Column(0, "id", INT), Column(0, "name", CHAR, 10)]
    },
    "file_path": os.path.join(context.get_data_dir(), "db1", "product.db")
  }
  open(os.path.join(context.get_data_dir(), context.get_schema_path()), 'w').close()
  shutil.rmtree("./datadir/db1")


def test_table_creation(setup):
  data = setup.get("data")
  file_path = setup.get("file_path")
  t = Table(**data)
  t.create()
  assert os.path.exists(file_path)