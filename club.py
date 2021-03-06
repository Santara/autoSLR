f = open("Results/keyword-frequency_list.csv",'r')

counts = {}
num_articles_occurred = {}

for line in f:
	line = line.strip()
	k, v = line.split(',')[0].strip(), int(line.split(',')[1].strip())
	if k in counts.keys():
		counts[k] += v
		num_articles_occurred[k] += 1
	else:
		counts[k] = v
		num_articles_occurred[k] = 1

output_f = open('Results/keywords-clubbed_across_documents.csv','w')
output_f.write("KEYWORD, TOTAL_TERM_FREQUENCY, DOCUMENT_FREQUENCY\n")
i=0
for key, value in sorted(counts.iteritems(), key=lambda (k,v): (v,k), reverse=True):
	if i < 100:
		i += 1
		output_f.write("%s, %s, %s\n" % (key, value, num_articles_occurred[key]))
	else:
		i += 1
	if key == "governance":
		print i, value, num_articles_occurred[key]

output_f.close()
