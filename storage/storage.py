import os

from constants import *

def insert(data):
  pass

def delete(column, value):
  pass

def update(column, value, **updates):
  pass

def select(**criteria):
  pass

def create_data_file():
  pass

def create_table():
  pass

def create_schema(name, **kwargs):
  # decide on datadir - for testing purpose
  data_dir = kwargs.get('data_dir', constants.DEFAULT_DATA_DIR)
  db_folder = os.path.join(data_dir, name)

  # check if a directory already exists
  if os.path.exists(database_folder):
    raise Exception("db folder already exists")
  # Check the schemata entry
  if _is_db_entry_present(name):
    raise Exception("db entry already present")

  # Create db folder and entry in schemata
  os.makedirs(name=db_folder)
  return 0
  
def _is_db_entry_present(db_name):
  schemata_path = os.path.join(DEFAULT_DATA_DIR, SCHEMATA_PATH )
  with open(schemata_path) as f:
    f.readlines().contains(db_name)