import json
import geocoder
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
            navigator.update_geolocation(city_table, row['id'], longitude, latitude)




if __name__ == '__main__':
    enrichment = GeoEnrichment('../static/config/connection_config.json')
    with open('../static/config/connection_config.json') as json_data_file:
        data = json.load(json_data_file)
    try:
        connection_prop = data['mysql']
        navigator = Navigator(connection_prop['user'], connection_prop['passwd'],
                          connection_prop['host'], connection_prop['db'])
        #navigator = Navigator('../static/config/connection_config.json')
    except ConnectionError:
        pass
    enrichment.enrich_cities('staedte_de_tiny', ['stadt'], navigator)



