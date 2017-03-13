import json

out1 = open('test/json/output')
output = open('mid2.txt', 'a')
lines = out1.readlines()
result = []
id = []
for line in lines:
    #print (line)
    l = json.loads(line)
    mid = l['id'].split('.')[0]
    print(mid)
    if mid not in id:
        print ("add")
        id.append(mid)
        result.append(l)
for x in range(len(result)):
    output.write(json.dumps(result[x]) + "\n")
