f = open('data.txt', 'r')
lines = f.readlines()
f.close()
out = ""

for i in lines:
	ShiftFlag = False
	data = i.split(':')
	if data[0] == "20":
		ShiftFlag = True
	diff = int(data[2], 16)
	if diff == int('00', 16):
		pass
	elif diff < int('1E', 16):
		if ShiftFlag:
			key = chr(ord('A')+diff-4)
		else:
			key = chr(ord('a')+diff-4)			
		out += key
	elif diff < int('27', 16):
		key = chr(ord('0')+diff-int('1D', 16))
		out += key
	elif diff == int('27', 16):
		out += chr(ord('0'))
	elif diff == int('2D', 16):
		if ShiftFlag:
			out += chr(ord('_'))
		else:
			out += chr(ord('-'))
	elif diff == int('30', 16):
		if ShiftFlag:
			out += chr(ord('}'))
		else:
			out += chr(ord(']'))
	elif diff == int('2f', 16):
		if ShiftFlag:
			out += chr(ord('{'))
		else:
			out += chr(ord('['))
	else:
		pass
print(out)