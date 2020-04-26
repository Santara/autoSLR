import os
import sys
directory = sys.argv[1]
outfile = open("key_phrases.csv","w")

files = {}

for filename in os.listdir(directory):

	text=[]
	with open(os.path.join(directory, filename)) as f:
		text=[l.strip() for l in f if len(l.strip())>2]
	data=''
	for t in text:
		if len(t.split()) > 1:
			data = data+'. '+t.strip()
	whitelist = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	answer = ''.join(filter(whitelist.__contains__, data))
	answer=' '.join(answer.split())

	import rake
	import operator
	rake_object = rake.Rake("/home/ashutosh/Sudeshna/RAKE-tutorial/data/stoplists/SmartStoplist.txt", 3,3,1)
	import pprint
	pp = pprint.PrettyPrinter()
	keywords = rake_object.run(answer)

	for entry in keywords:
		outfile.write("%s, %s\n" % (entry[0], str(entry[1])) )

outfile.close()
