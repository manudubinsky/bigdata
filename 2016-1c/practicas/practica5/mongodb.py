import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.test

for a in db.tweets.find({"id":714944943698100224}):
    print a


for a in db.tweets.find({"geo": {"$ne":None}},{"user.name":1,"_id":0,"geo":1}):
    print a


