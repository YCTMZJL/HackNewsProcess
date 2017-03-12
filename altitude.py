from geopy.geocoders import Nominatim

gps=Nominatim()
map = {}
f = open("test.txt")
lines = f.readlines()
for line in lines:
	line = line.strip()
	words = line.split("\t")
	location = gps.geocode(words[0])
	if location != None:
		alti = []
		alti.append(location.longitude)
		alti.append(location.latitude)
		map[words[0]] = alti
out = open("altiresult.txt", "a")
out.write(str(map))