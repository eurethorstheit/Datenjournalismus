#!/usr/bin/env python
import json

import click, toml
import pandas as pd
import sqlalchemy
import sys, os
from dbconfig import dbconfig, dtypes
from pydb import Navigator
from pprint import pprint
import pandas as pd

@click.command()
@click.option('--write-to-table','-w', default="", help='Writes to an new table')
@click.option('--get-table','-r', default="", help='Reads table and prints it out as pandas')
@click.option('--get-query','-q', default="", help='Reads query and prints it out as pandas')
def start(**kwargs):
    """Simple database manager for the MDR-Project."""

    if kwargs['write_to_table']:
        dbconfig.table_write = True
        dbconfig.table_replace = True
        dbconfig.table_csv_file = kwargs['write_to_table']
        dbconfig.table_name = os.path.basename(dbconfig.table_csv_file).split('.')[0]
        dbconfig.table_dtypes = dtypes[dbconfig.table_name]

        ''' Check if csv file exists'''
        if not os.path.isfile(dbconfig.table_csv_file):
            exit("No such csv file exists within csvfiles folder")

    elif kwargs['get_table']:
        dbconfig.table_name = kwargs['get_table']
    elif kwargs['get_query']:
        dbconfig.table_name = kwargs['get_query']

    else:
        exit("Nothing chosen")
    with open('static/config/connection_config.json') as json_data_file:
        data = json.load(json_data_file)
        connection_prop = data['mysql']
    nav = Navigator(connection_prop['user'], connection_prop['passwd'],
                      connection_prop['host'], connection_prop['db'])

    if kwargs['write_to_table']:
        df = pd.read_csv(dbconfig.table_csv_file)
        print(df)
        print("Name of table: " + str(dbconfig.table_name))
        print("Data types:" + str(dbconfig.table_dtypes))
        print("This Data will be inserted into Database and replaces existing table\n")
        input('Input for proceed ...')

        nav.create_table_from_pandas(df, dbconfig.table_name, dbconfig.table_dtypes)

    if kwargs['get_table']:
        data = nav.get_data_from_db_json(dbconfig.table_name)
        print(data)

    if kwargs['get_query']:
        data = nav.get_query_data_from_db(dbconfig.table_name,'Stadt','Augsburg')
        print(data)


if __name__ == '__main__':
    start()

'''
Iterieren über types muss noch gmacht werden
'''