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
            geocode_result = geocoder.mapquest(query, key= self.mapquest_key)
            #latitude = json.loads(geocode_result.json)[0]['lat']
            #longitude = json.loads(geocode_result.json)[0]['lng']
            #print(latitude)
            #print(longitude)
            #navigator.update_geolocation(city_table, row['id'], longitude, latitude)
            print(geocode_result)



if __name__ == '__main__':
    enrichment = GeoEnrichment('../static/config/connection_config.json')
    navigator = Navigator('../static/config/connection_config.json')
    enrichment.enrich_cities('staedte_de_tiny', ['stadt'], navigator)



