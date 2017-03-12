import json

file = open("mid1.txt")
lines = file.readlines()
full = []
for line in lines:
	line = line.strip()
	l = json.loads(line)
	full.append(l['id'])
print(full)
file = open("rec1.txt")
lines = file.readlines()
words = lines[0].split("', '")
result = []
for word in words:
	if word in full:
		result.append(word)
out = open("recommand1.txt", "a")
out.write(str(result))