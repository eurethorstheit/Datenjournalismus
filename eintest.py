#!/usr/bin/env python

from pydb import Navigator
'''
nav = Navigator()

data = nav.get_data_from_db('staedte_de_tiny')

print(data)


nav.kleinertest()

'''
item="my_table"
table=""
value=""

sql = """
              SELECT
                danceability, energy, loudness, speechiness, acousticness,
                instrumentalness, liveness, valence, tempo, activity
              FROM songs s, users u, song_user su
              WHERE
                activity IS NOT NULL AND
                s.id = su.song_id AND
                su.user_id = u.id AND
                u.telegram_user_id = {}
        """.format("Hallo")

def printsql():
	print(sql2)

sql2 = """
              SELECT
                {}
              FROM {}
              WHERE
		item = {}
        """.format('Stadt','staedte_de_tiny','staedte_de_tiny','Augsburg')



printsql()


