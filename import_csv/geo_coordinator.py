
import mysql.connector
import json

class GeoCoordinator:

    def __init__(self, connection:mysql.connector):
        self.connection= connection

    def get_geocode_for_city(self, city_table, city_id):
        sql = 'Select lng, lat from {} where id = {}'.format(city_table, city_id)
        print(sql)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        geo = dict()
        for row in cursor:
            print(row)
            geo['lng'] = row[0]
            geo['lat'] = row[1]
        json_ego = json.dumps(geo)
        cursor.close()
        return json_ego

    def get_geocodes(self, city_table):
        sql = 'Select lng, lat from {}'.format(city_table)
        print(sql)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        points =[]
        for row in cursor:
            print(row)
            geo = dict()
            geo['lng'] = row[0]
            geo['lat'] = row[1]
            points.append(geo)
        json_ego = json.dumps(points)
        cursor.close()
        return json_ego
