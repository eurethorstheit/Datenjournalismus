from sqlalchemy.types import Integer, Text, String, DateTime, Float, Numeric, NUMERIC

class dbconfig:
    dbname = ""
    table_name = ""
    table_write = False
    table_replace = False
    table_csv_file = ""
    table_dtypes = None

dtypes = {
    'staedte_de_tiny': {'Stadt': String(60),
                  'PLZ': String(5)
                  },
    'staedte_de': {'Stadt': String(60),
                  'PLZ': String(60),
                  'Bundesland': String(60),
                  'Landkreis': String(60)
                  }
    }
