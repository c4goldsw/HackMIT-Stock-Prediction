import json


jStruct = []
with open("appl.json", "r") as appl:
	jStruct = json.loads(appl.read())['data']

appl_len = len(jStruct)

for i in range(len(jStruct) -1, -1, -1):
	if jStruct[i]['bullish_percent'] == 0.0 and jStruct[i]['bearish_percent'] == 0.0:
		del(jStruct[i])

with open("appl_parse.json",'w') as appl:
	appl.write(json.dumps(jStruct))


appl_parse_len = len(jStruct)

print("appl len: {}, appl_parse len: {}".format(appl_len, appl_parse_len))

#====================================================================================

with open("fb.json", "r") as fb:
	jStruct = json.loads(fb.read())['data']

fb_len = len(jStruct)

for i in range(len(jStruct) -1, -1, -1):
	if jStruct[i]['bullish_percent'] == 0.0 and jStruct[i]['bearish_percent'] == 0.0:
		del(jStruct[i])

with open("fb_parse.json", "w") as fb:
	fb.write(json.dumps(jStruct))

fb_parse_len = len(jStruct)

print("fb len: {}, fb len: {}".format(fb_len, fb_parse_len))

#====================================================================================

with open("tsl.json", "r") as tsl:
	jStruct = json.loads(tsl.read())['data']

tsl_len = len(jStruct)

for i in range(len(jStruct) -1, -1, -1):
	if jStruct[i]['bullish_percent'] == 0.0 and jStruct[i]['bearish_percent'] == 0.0:
		del(jStruct[i])

with open("tsl_parse.json", "w") as tsl:
	tsl.write(json.dumps(jStruct))

tsl_parse_len = len(jStruct)

print("tsl len: {}, tsl len: {}".format(tsl_len, tsl_parse_len))
