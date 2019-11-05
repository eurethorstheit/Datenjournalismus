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

    def kleinertest(self):
        '''
        Ein kleiner  Test
        '''
        print("Test")

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

    def get_query_data_from_db(self,table,item='Stadt',value='Augsburg'):
        ''' Funzt noch nicht '''

        sql = ('SELECT Stadt, PLZ FROM staedte_de_tiny WHERE Stadt=Augsburg')
        df = pd.read_sql_query(
            sql=sql,
            con=self.engine)
        return df

    def insert_data_into_db(self):
        self.data.to_sql(con=self.cnx, name='table_name_for_df', if_exists='replace')