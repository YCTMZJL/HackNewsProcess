import json
import urllib2
import ssl

input = open('stories')
output = open('output.txt', 'a')
lines = input.readlines()
for l in lines:
	line = json.loads(l)
	if line.has_key('type'):
		if (line['type'] == 'story'):
			if line.has_key('text'):
				result = {}
				result['id'] = line['id']
				result['content'] = line['text']
				str = json.dumps(result)
				output.write(str)
			if line.has_key('url'):
				context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
				hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'pl-PL,pl;q=0.8','Connection': 'keep-alive'}
				req = urllib2.Request('http://www.mynameisbreanne.com/case-study-taa/', headers = hdr)
				try:
					resp = urllib2.urlopen(req, context = context)
					strHtml = resp.read()
					print (line['id'] + ":200 OK")
					result = {}
					result['id'] = line['id']
					result['content'] = strHtml
					str = json.dumps(result)
					output.write(str)
				except urllib2.HTTPError as e:
					print (line['id'])
					print (e.code)
				except urllib2.URLError as e:
					print("Failed to reach the server")
					print(e.reason)
output.close()
