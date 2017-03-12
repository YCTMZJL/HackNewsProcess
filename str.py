f = open("test.txt")
lines = f.readlines()
str = '['
for line in lines:
	line = line.strip()
	words = line.split("\t")
	str += '{name: "' + words[0] + '", value:' + words[1] + '}, '
str += ']'
print(str)
out = open("str.txt", "a")
out.write(str)