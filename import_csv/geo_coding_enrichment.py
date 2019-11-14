import json
import geocoder

from import_csv.db_manager import DbManager
from pydb import Navigator



GOOGLE_URL = "https://maps.googleapis.com/maps/api/geocode/json?address="

class GeoEnrichment:
    '''
    This class is add longitude and latitude information using google geocoding service
    '''


    def __init__(self, config):
        with open(config) as json_data_file:
            data = json.load(json_data_file)
            self.mapquest_key = data['mapquest_key']

    def enrich_cities(self, city_table, columns: list, db_navigator: Navigator):
        city_data_frame = db_navigator.get_data_from_db(city_table)

        for index, row in city_data_frame.iterrows():
            query = ''
            for column_name in columns:
                query += row[column_name] + ' '
            query += ' Germany'
            query = query.strip()
            print(query)
            geocode_result = geocoder.mapquest(query, key=self.mapquest_key)
            print(geocode_result.json)
            latitude = geocode_result.json['lat']
            longitude = geocode_result.json['lng']
            print(latitude)
            print(longitude)
            db_navigator.update_geolocation(city_table, row['id'], longitude, latitude)

    def enrich_cities_connector(self, city_table, columns: list, connector: DbManager):
        city_data_frame = connector.get_data_from_db(city_table)
        cursor = connector.connection.cursor()
        sql = """UPDATE {} set lng = %s, lat=%s where id = %s""".format(city_table)
        for index, row in city_data_frame.iterrows():
            query = ''
            for column_name in columns:
                query += row[column_name] + ' '
            query += ' Germany'
            query = query.strip()
            print(query)
            geocode_result = geocoder.mapquest(query, key=self.mapquest_key)
            print(geocode_result.json)
            latitude = geocode_result.json['lat']
            longitude = geocode_result.json['lng']
            print(latitude)
            print(longitude)
            cursor.execute(sql, (row['id'], longitude, latitude))
        cursor.close()


if __name__ == '__main__':
    enrichment = GeoEnrichment('../static/config/connection_config.json')
    try:
        db_manager = DbManager.from_config_file('../static/config/connection_config.json')
        #navigator = Navigator('../static/config/connection_config.json')
    except ConnectionError:
        pass
    enrichment.enrich_cities_connector('staedte_de_tiny', ['stadt'], db_manager)
    #enrichment.enrich_cities('staedte_de', ['stadt'], navigator)



