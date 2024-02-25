from storage import storage

import pytest
import shutil

@pytest.fixture
def db_with_custom_datadir():
  print("Clean storage")
  database_name = "db1"
  yield {"db_name": "db1", "data_dir": "test_datadir"}
  shutil.rmtree("./test_datadir/db1")


def test_create_schema_with_custom_datadir(db_with_custom_datadir):
  data = db_with_custom_datadir
  assert 0 == storage.create_schema(data.get('db_name'), data_dir=data.get('data_dir'))

@pytest.fixture
def db_without_datadir():
  print("Clean storage")
  database_name = "db1"
  yield database_name
  shutil.rmtree("./datadir/db1")

def test_create_schema_with_default_datadir(db_without_datadir):
  assert 0 == storage.create_schema(db_without_datadir)

def test_exception_if_db_folder_already_present():
  storage.create_schema(db_without_datadir)
  with pytest.raises(Exception()):
    storage.create_schema(db_without_datadir)
