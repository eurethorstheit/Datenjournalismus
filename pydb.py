#!/usr/bin/env python
import json

import pandas as pd
import sqlalchemy
import sys


class Navigator():


    def __init__(self, user, pw,host, database):
        self.engine = sqlalchemy.create_engine(
            'mysql+pymysql://{}:{}@{}:3306/{}'.format(user, pw, host, database),
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
            if_exists='append',
            dtype=dtypes,
        )

    def get_data_from_db(self, _table):
        ''' Returns Data from table as dictionary without index
        :table table-name
        :return dict
        '''
        df = pd.read_sql_table(_table, self.engine)
        return df

    def get_data_from_db_json(self, _table):
        ''' Returns Data from table as dictionary without index
        :table table-name
        :return dict
        '''
        df = pd.read_sql_table(_table, self.engine)
        df['id'] = df['id'].apply(lambda old_id: 'c_' + str(old_id))
        #df = df.rename({'id': 'DT_RowId'}, axis='columns')
        result = self.json_extension(df.to_json(orient='records'), len(df.index))
        print(result)
        return result

    def json_extension(self, json_data_result, row_count):
        json_string = '{{"draw":1, "recordsTotal": {}, "recordsFiltered": {}, "data":{}}}'\
            .format(row_count, row_count, json_data_result)
        return json_string

    def get_query_data_from_db(self, table, item='Stadt', value='Augsburg'):
        ''' Funzt noch nicht '''

        sql = ('SELECT Stadt, PLZ FROM staedte_de_tiny WHERE Stadt="Augsburg"')
        df = pd.read_sql_query(
            sql=sql,
            con=self.engine)
        return df

    def insert_data_into_db(self):
        self.data.to_sql(con=self.cnx, name='table_name_for_df', if_exists='replace')
