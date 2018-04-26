infile = open("sud3_results.csv","r")
outfile = open("sud4_results.csv","w")

keywords = infile.readline().strip().split(",")[1:]
outfile.write("%s, %s" % ("filename", ",".join("Environment+Social+Economic", "Environment+Social+Economic+Cultural", "Environment+Social+Economic+Cultural+Institutional")))

three_pillars_keywords = ["environmental", "housing", "energy", "water", "social", "local", "community", "public", "economic"]
four_pillars_keywords = three_pillars_keywords + ["cultural", "culture"]
five_pillar_keywords = four_pillars_keywords + ["urban", "planning"]

for line in infile.readlines():
	data = line.split(",")
	filename = data[0]
	numerical = [int(entry) for entry in data[1:]]