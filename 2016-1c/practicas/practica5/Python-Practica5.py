from pymongo import MongoClient

client = MongoClient()
db = client.test


print "===================="
print 'Punto 1'
print "===================="

cursor = db.tweets.find({'user.id': 227188464}, {'user.screen_name': 1, 'text': 1, '_id': 0})

for document in cursor:
	print document

print "===================="
print 'Punto 2'
print "===================="

cursor = db.tweets.find({"geo": {"$ne":None}}, {'user.name': 1, 'geo': 1, '_id': 0})

for document in cursor:
	print document

print "===================="
print 'Punto 3'
print "===================="
"""
> var map = function() { emit(this.lang,1);};
> var reduce = function(language, value) {return (Array.sum(value));};
> db.tweets.mapReduce(map,reduce,{out:"testMapReduce"})
"""

cursor = db.tweets.aggregate(
								[
									{'$group': {'_id': '$lang', 'count': {'$sum': 1}}}
								]
							)

#Nota: el campo '_id' en este caso se utiliza para indicarle al 'group' bajo que campo agrupar.

for document in cursor:
	print document