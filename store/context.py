import os

DEFAULT_DATA_DIR="./datadir"
SCHEMATA_PATH="sys/schemata.csv"

class Context():
  
  def __init__(self,  **context_overrides) -> None:
    default_context = {
      "data_dir": DEFAULT_DATA_DIR,
      "schema_path": SCHEMATA_PATH
    }

    self.context = default_context
    self.context.update(**context_overrides)
  
  def get_data_dir(self):
    return self.context.get("data_dir")
  
  def get_schema_path(self):
    return self.context.get("schema_path")
  
  def get_schemata_path(self):
    return os.path.join(DEFAULT_DATA_DIR, self.get_schema_path())