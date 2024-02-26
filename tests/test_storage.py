from store import storage

import pytest
import shutil
import os
from store.storage import DEFAULT_DATA_DIR, SCHEMATA_PATH

@pytest.fixture
def db_with_custom_datadir():
  print("Clean storage")
  yield {"db_name": "db1", "data_dir": "test_datadir"}
  open(os.path.join(DEFAULT_DATA_DIR, SCHEMATA_PATH), 'w').close()
  shutil.rmtree("./test_datadir/db1")


def test_create_schema_with_custom_datadir(db_with_custom_datadir):
  data = db_with_custom_datadir
  assert 0 == storage.create_schema(data.get('db_name'), data_dir=data.get('data_dir'))

@pytest.fixture
def db_without_datadir():
  print("Clean storage")
  database_name = "db1"
  yield database_name
  open(os.path.join(DEFAULT_DATA_DIR, SCHEMATA_PATH), 'w').close()
  shutil.rmtree("./datadir/db1")


def test_create_schema_with_default_datadir(db_without_datadir):
  assert 0 == storage.create_schema(db_without_datadir)

@pytest.fixture
def db_folder_already_exists():
  print("Clean storage")
  os.makedirs("./datadir/db1")
  database_name = "db1"
  yield database_name
  open(os.path.join(DEFAULT_DATA_DIR, SCHEMATA_PATH), 'w').close()
  shutil.rmtree("./datadir/db1")

def test_exception_if_db_folder_already_present(db_folder_already_exists):
  with pytest.raises(Exception) as e:
    storage.create_schema(db_folder_already_exists)
  assert "db folder already exists" in str(e.value)

@pytest.fixture
def db_entry_already_exists():
  with open(os.path.join(DEFAULT_DATA_DIR, SCHEMATA_PATH), 'w') as f:
    f.write("db1")
  database_name = "db1"
  yield database_name
  open(os.path.join(DEFAULT_DATA_DIR, SCHEMATA_PATH), 'w').close()

def test_exception_if_db_entry_already_present(db_entry_already_exists):
  with pytest.raises(Exception) as e:
    storage.create_schema(db_entry_already_exists)
  print(e.value)
  assert "db entry already present" in str(e.value)
