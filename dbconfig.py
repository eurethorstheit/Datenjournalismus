from sqlalchemy.types import Integer, Text, String, DateTime, Float, Numeric, NUMERIC

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

class dbconfig:
    dbname = "journalDB"
    table_name = "city"
    table_write = True
    table_replace = False
    table_csv_file = ""
    table_dtypes = dtypes['staedte_de_tiny']


