import os

DEFAULT_DATA_DIR="./datadir"
SCHEMATA_PATH="sys/schemata.csv"

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

def create_table(db, table_name, **column_details):
  pass
  
def create_schema(name: str, **kwargs: dict) -> int:
  # decide on datadir - for testing purpose
  data_dir = kwargs.get('data_dir', DEFAULT_DATA_DIR)
  db_folder = os.path.join(data_dir, name)
  
  # Check the schemata entry
  if _is_db_entry_present(name):
    raise Exception("db entry already present")

  # check if a directory already exists
  if os.path.exists(db_folder):
    raise Exception("db folder already exists")

  # Create db folder and entry in schemata
  os.makedirs(name=db_folder)
  schemata_path = os.path.join(DEFAULT_DATA_DIR, SCHEMATA_PATH)
  with open(schemata_path, "a") as f:
    f.writelines(name+"|")
  return 0
  
def _is_db_entry_present(db_name: str) -> bool:
  schemata_path = os.path.join(DEFAULT_DATA_DIR, SCHEMATA_PATH)
  with open(schemata_path) as f:
    return db_name in f.readline().split("|")