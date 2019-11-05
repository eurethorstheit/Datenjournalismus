#!/usr/bin/env python

import pandas as pd
import sqlalchemy
import sys

class Navigator():
    def __init__(self):
        self.engine = sqlalchemy.create_engine(
            'mysql+pymysql://admin:mdr@localhost:3306/journalDB',
            echo=False
        )
        '''
        self.csv_file = csv_file
        self.table = table
        self.dtypes = dtypes
        '''
    def create_table_from_pandas(self, df, table_name, dtypes):

        df.to_sql(
            name=table_name,
            con=self.engine,
            index=False,
            if_exists='replace',
            dtype=dtypes
        )

    def get_data_from_db(self,_table):
        ''' Returns Data from table as dictionary without index
        :table table-name
        :return dict
        '''
        df = pd.read_sql_table(_table, self.engine)
        return df

    def connect_to_db(self,name_database):
        ''' Das hier ist nun vermutlich obsolet'''
        self.cnx = mysql.connector.connect(user='admin', password='journallie',
                                      host='127.0.0.1',
                                      database=name_database)

    def insert_data_into_db(self):
        self.data.to_sql(con=self.cnx, name='table_name_for_df', if_exists='replace')

    def get_data_from_csv(self,_csvfile):
        ''' Duplikat '''
        self.data = pandas.read_csv(_csvfile)
        self.data = pandas.DataFrame(data=self.data)

    def testdata(self):
        print(self.csv_file)
        print(self.table)
        print(self.dtypes)
#nav = Navigator() # Create Object
'''
print("Read toml")
_toml = sys.argv[1]

_toml_file = toml.load(_toml)
'''
