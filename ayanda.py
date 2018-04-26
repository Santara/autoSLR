#pdfminer_text = open("AlphaGo.txt")
# r = Rake()
# pp = pprint.PrettyPrinter()
# r.extract_keywords_from_text(pdfminer_text)
# pp.pprint(r.get_ranked_phrases_with_scores()[:20])

import os
import sys
directory = sys.argv[1]

NUM_KEYWORDS_FROM_EACH_FILE = 25

files = {}
num_keywords_extracted_f = open("num_keywords_extracted.csv","a")

for filename in os.listdir(directory):
	if filename.endswith(".pdf"):
		filename_txt = filename.split('.')[0]+'.txt'
		if os.path.exists(os.path.join(directory,'text_papers/',filename_txt)):
			continue
		try:
			os.system("pdf2txt.py %s > %s" % (os.path.join(directory,filename), os.path.join(directory,'text_papers/',filename_txt)))
		except:
			print "Could not read: %s" % (filename)	
			continue

		#Preprocessing
		text=[]
		with open(os.path.join(directory,'text_papers/',filename_txt)) as f:
			text=[l.strip() for l in f if len(l.strip())>2]
		data=''
		for t in text:
			if len(t.split()) > 1:
				data = data+'. '+t.strip()
		whitelist = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')
		answer = ''.join(filter(whitelist.__contains__, data))
		answer=' '.join(answer.split())

		# print answer
		# from rake_nltk import Rake 
		import rake
		import operator
		rake_object = rake.Rake("/home/ashutosh/Sudeshna/RAKE-tutorial/data/stoplists/SmartStoplist.txt", 3,1,1)
		import pprint
		# r = Rake()
		pp = pprint.PrettyPrinter()
		# r.extract_keywords_from_text(answer)
		keywords = rake_object.run(answer)
		keywords = [k[0] for k in keywords]
		# pp.pprint(r.get_ranked_phrases_with_scores()[:50])

		counts = {k:0 for k in keywords}

		# print counts
		for word in answer.split():
			if word in keywords:
				counts[word] += 1

		output_f = open('sud1_results.csv','a')
		i=0
		for key, value in sorted(counts.iteritems(), key=lambda (k,v): (v,k), reverse=True):
			if i < NUM_KEYWORDS_FROM_EACH_FILE:
				i += 1
				output_f.write("%s, %s\n" % (key, value))

		output_f.close()
		num_keywords_extracted_f.write("%s, %s\n" %(filename_txt, min(len(counts.keys()), NUM_KEYWORDS_FROM_EACH_FILE)))
		print "Processed: %s, %s" % (filename_txt, min(len(counts.keys()), NUM_KEYWORDS_FROM_EACH_FILE))

	else:
		continue

num_keywords_extracted_f.close()