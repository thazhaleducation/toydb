from store.context import Context

def test_return_default_context():
  assert Context().get_data_dir() == "./datadir"
  assert Context().get_schema_path() == "sys/schemata.csv"
  assert Context().get_schemata_path() == "./datadir/sys/schemata.csv"