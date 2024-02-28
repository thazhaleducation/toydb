from .column import Column
from .context import Context
import os


class Table():
  def __init__(self, db: str, name: str, columns: list[Column], context: Context = Context()):
    self.db = db
    self.name = name
    self.columns = columns
    self.context = context

  def file(self):
    return f"{self.context.get_data_dir()}/{self.db}/{self.name}.db"
  
  def create(self):
    # check for entry in tables.csv
    # Create a table.db file
    with open(self.file(), 'w'):
      pass
    # Add an entry in tables.csv if not already exists for the same db
    # Add columns mapping in the columns csv
