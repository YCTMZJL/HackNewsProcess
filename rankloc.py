import json

f1 = open("loc/mid210025337.html_loc.json")
lines = f1.readlines()
words1 = []
words2 = []
map = {}
for line in lines:
	words1 = line.split('", "')
f2= open("loc/mid24016677.html_loc.json")
lines = f2.readlines()
for line in lines:
	words2 = line.split('", "')
f = open("highscoreLoc2.json")
lines = f.readlines()
for line in lines:
	line = line.strip()
	w = line.split("': ")
	key = w[0][2: len(w[0])].lower()
	value = w[1][0: len(w[1]) - 1]
	if key in map.keys():
		num = map[key]
		num = num + int(value)
		map[key] = num
	else:
		map[key] = int(value)
for word in words1:
	word = word.lower()
	if word in map.keys():
		num = map[word]
		num = num + 1
		map[word] = num
	else:
		map[word] = 1
for word in words2:
	word = word.lower()
	if word in map.keys():
		num = map[word]
		num = num + 1
		map[word] = num
	else:
		map[word] = 1
ranked = sorted(map.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
out = open("result4.txt", "a")
for key in ranked:
	out.write(key[0] + "\t" + str(key[1]) + "\n")