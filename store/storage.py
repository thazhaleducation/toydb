import os
from .context import Context

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
  
def create_schema(name: str, context:Context = Context(), **kwargs: dict) -> int:
  # decide on datadir - for testing purpose
  db_folder = os.path.join(context.get_data_dir(), name)
  
  # Check the schemata entry
  if _is_db_entry_present(name, context):
    raise Exception("db entry already present")

  # check if a directory already exists
  if os.path.exists(db_folder):
    raise Exception("db folder already exists")

  # Create db folder and entry in schemata
  os.makedirs(name=db_folder)
  with open(context.get_schemata_path(), "a") as f:
    f.writelines(name+"|")
  return 0
  
def _is_db_entry_present(db_name: str, context: Context) -> bool:
  with open(context.get_schemata_path()) as f:
    return db_name in f.readline().split("|")