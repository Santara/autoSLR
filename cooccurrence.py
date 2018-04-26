file1 = open("sud2_results.csv",'r')

outfile = open("sud3_results.csv", "w")

keywords = [line.strip().split(',')[0].strip() for line in file1.readlines()]
keywords = keywords[:25]

print keywords

import sys
import os

directory = sys.argv[1]

outfile.write("%s, %s\n" %("filename", ','.join(keywords)))

for filename in os.listdir(directory):
	#Preprocessing
	text=[]
	with open(os.path.join(directory,filename)) as f:
		text=[l.strip() for l in f if len(l.strip())>2]
	data=''
	for t in text:
		if len(t.split()) > 1:
			data = data+'. '+t.strip()
	whitelist = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	answer = ''.join(filter(whitelist.__contains__, data))
	answer=' '.join(answer.split())

	occurrence_count = {k:0 for k in keywords}
	for word in answer.split():
		if word in keywords:
			occurrence_count[word] += 1
	print filename, ":\n", occurrence_count, "\n\n"
	outfile.write("%s, %s\n" % (filename, ','.join([str(occurrence_count[k]) for k in keywords])))

file1.close()
outfile.close()