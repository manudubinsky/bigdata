#!/usr/bin/python
# -*- coding: utf-8 -*-

# Para mas info de como funciona el tema de la interacción de python con postgres, fijate este link que te explica todo: http://zetcode.com/db/postgresqlpythontutorial/
import psycopg2
import sys
import json



con = None

tweets_data_path = 'miArgentina.txt'

tweets_file = open(tweets_data_path, "r")

try:     
	con = psycopg2.connect(database='postgres', user='postgres', host='localhost',password='Labtec1745') ;
	cur = con.cursor();
	
	for line in tweets_file:
		try:
			linea = json.loads(line);
			keys = linea.viewkeys();
			if ('entities' in keys):
				entities = linea['entities'];

			try:
				#TWEET
				if ('retweeted_status' in keys):
					rs =str(unicode(linea['retweeted_status']['id']));
				else:
					rs =str(0);
				cur.execute("INSERT INTO tweet(tweet_id, user_id, tweet_text, created_at, original_tweet_id, retweet_count) VALUES ("+str(unicode(linea['id']))+","+str(unicode(linea['user']['id']))+",'"+unicode(linea['text']).replace("'"," ")+"','"+unicode(linea['created_at'])+"',"+rs+","+str(unicode(linea['retweet_count']))+")");
				con.commit();
				#USER
				cur.execute("INSERT INTO usuario(user_id, screen_name, name, profile_image_url, location, url, description, created_at, followers_count, friends_count, statuses_count, time_zone, lang)  SELECT "+str(unicode(linea['user']['id']))+",'"+unicode(linea['user']['screen_name'])+"','"+unicode(linea['user']['name']).replace("'"," ")+"','"+unicode(linea['user']['profile_image_url'])+"','"+unicode(linea['user']['location'])+"','"+unicode(linea['user']['url'])+"','"+unicode(linea['user']['description']).replace("'"," ")+"','"+unicode(linea['user']['created_at'])+"',"+str(unicode(linea['user']['followers_count']))+","+str(unicode(linea['user']['friends_count']))+","+str(unicode(linea['user']['statuses_count']))+",'"+unicode(linea['user']['time_zone'])+"','"+unicode(linea['user']['lang'])+"' WHERE NOT EXISTS (SELECT 1 FROM usuario WHERE user_id='"+str(unicode(linea['user']['id']))+"')");
				con.commit();
				#HASHTAG
				if ('hashtags' in linea['entities'].viewkeys()):
					hashtag =entities['hashtags'];  
					for ht in hashtag:
						cur.execute("INSERT INTO hashtag(hashtag_text) SELECT '"+unicode(ht['text'])+"'  WHERE NOT EXISTS (SELECT 1 FROM hashtag WHERE hashtag_text='"+unicode(ht['text'])+"')");
						con.commit();
						cur.execute("INSERT INTO tweet_hashtag(hashtag_id, tweet_id) VALUES ((SELECT hashtag_id FROM hashtag ORDER BY hashtag_id DESC LIMIT 1),"+str(unicode(linea['id']))+")");
						con.commit();
				#MEDIA
				if ('media' in linea['entities'].viewkeys()):
					media =entities['media'];
					for med in media:
						cur.execute("INSERT INTO media(type, url) VALUES ('"+unicode(med['type'])+"','"+unicode(med['url'])+"')");
						con.commit();
						cur.execute("INSERT INTO tweet_media(media_id, tweet_id) VALUES ((SELECT media_id FROM media ORDER BY media_id DESC LIMIT 1),"+str(unicode(linea['id']))+")");
						con.commit();
			except psycopg2.DatabaseError, e:
				print 'Error %s' % e
		except Exception, e:
			print e;

except psycopg2.DatabaseError, e:
	print 'Error %s' % e    
	sys.exit(1)
	
	
finally:
	if con:
		con.close()
