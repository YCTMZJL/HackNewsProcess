import json
import urllib2
import ssl
import os

input = open('sep4')
output = open('output4.txt', 'a')
url = open('url3', 'a')
lines = input.readlines()
i = 0
for l in lines:
	print (i)
	i = i + 1
	line = json.loads(l)
	if line.has_key('type'):
		print (line['id'])
		if (line['type'] == 'story'):
			if line.has_key('text'):
				result = {}
				result['id'] = line['id']
				result['content'] = line['text']
				str = json.dumps(result)
				output.write(str)
				output.write("\n")
			if line.has_key('url'):
				os.system("curl --connect-timeout 5 -o result4/" + line['id'] + ".html " + line['url'])
output.close()
