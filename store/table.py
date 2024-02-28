from column import Column

class Table():
  def __init__(self, db, name, columns: list[Column], file):
    self.name = name
    self.columns = columns
    self.file = file

  def create(self):
    pass
    # check for entry in tables.csv
    # Create a db file
    # Add an entry in tables.csv if not already exists for the same db
    # Add columns mapping in the columns csv
