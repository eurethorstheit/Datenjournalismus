import json

import mysql.connector
import pandas as pd
import import_csv.insert_statements as stmt
import sqlalchemy

class DbManager:

    def __init__(self, user, pw, host, database, port=3306):
        self.connection = mysql.connector.connect(host=host, user=user, passwd=pw, port=port, database=database)
        self.engine = sqlalchemy.create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}'.format(user, pw, host, port, database),
            echo=False
        )

    @classmethod
    def from_config_file(cls, config_file):
        with open(config_file) as json_data_file:
            data = json.load(json_data_file)
            connection_prop = data['mysql']
            return DbManager(connection_prop['user'], connection_prop['passwd'],
                                  connection_prop['host'], connection_prop['db'])


    def init_tables(self, sql_script):
        with open(sql_script) as f:
            sql_file = f.read()
            f.close()
            queries = sql_file.split(";")
            cursor = self.connection.cursor()
            for q in queries:
                cursor.execute(q)
            self.connection.commit()
            cursor.close()

    def insert_data(self, sql_statement, csv_data_frame, selected_columns=None):
        '''
        import an arbitrary panda data frame that corresponds to the sql statement. The number of columns of the data
        frame must be equal to the number of place_holder
        :param sql_statement:
        :param csv_data_frame:
        :return:
        '''
        df = pd.read_csv(csv_data_frame, sep=";")
        cursor = self.connection.cursor()
        for index, row in df.iterrows():
            if selected_columns is not None:
                values = []
                for c_index in selected_columns:
                    values.append(row[c_index])
                t = tuple(values)
                print(t)
            else:
                t = tuple(row)
            cursor.execute(sql_statement, t)
        self.connection.commit()
        cursor.close()


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
        result = self.json_extension(df.to_json(orient='records'), len(df.index))
        return result

    def json_extension(self, json_data_result, row_count):
        json_string = '{{"draw":1, "recordsTotal": {}, "recordsFiltered": {}, "data":{}}}'\
            .format(row_count, row_count, json_data_result)
        return json_string

if __name__ == '__main__':

    db_manager = DbManager.from_config_file('../static/config/connection_config.json')
    db_manager.init_tables('../sql_scripts/create_tables.sql')
    db_manager.insert_data(stmt.INSERT_CITY_TINY, '../csvfiles/staedte_de_tiny.csv')
    db_manager.insert_data(stmt.INSERT_CITY_DE, '../csvfiles/staedte_de.csv', [1,2,3,4])
