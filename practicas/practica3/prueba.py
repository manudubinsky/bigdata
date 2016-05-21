import json

tweets_data_path = 'sample.txt'

tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
	#try:
	print line
	tweet = json.loads(line)
	for k in tweet.keys():
		print k + ":" + str(type(tweet[k]))
	print "\n********\n"
