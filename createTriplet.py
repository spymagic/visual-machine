
file = open("train_triplets.txt")

dict = {};
for line in file:
	linelist = line.split("\t");
	if(dict.has_key(linelist[0])):
		count=0;
		if(dict[linelist[0]]>count):
			count = dict[linelist[0]]

	else:
#		try:
			dict[linelist[0]] = linelist[2]
#		except:
#			continue

	print line
file.close()