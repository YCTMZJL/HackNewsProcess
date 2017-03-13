import json

out1 = open('output')
out2 = open('out2.txt')
output = open('mid1.txt', 'a')
lines = out1.readlines()
id = []
imgUrl = {}
i = 0
for line in lines:
    #print (line)
    l = json.loads(line)
    mid = l['id'].split('.')[0]
    imgUrl[mid] = l['imgUrl']
    print(mid)
    if mid not in id:
        id.append(mid)
lines = out2.readlines()
for line in lines:
    print(l['id'])
    l = json.loads(line)
    id.append(l['id'])
result = []
out = open("../../full_201510_000000000000")
lines = out.readlines()
for line in lines:
    l = json.loads(line)
    if l['id'] in id:
        print (l['id'])
        if l['id'] in imgUrl:
            l['imgUrl'] = imgUrl[l['id']]
        result.append(l)
for x in range(len(result)):
    output.write(json.dumps(result[x]) + "\n")
