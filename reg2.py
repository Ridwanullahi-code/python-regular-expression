import re
def Phone_number(a):
	pattern = re.compile(r'\d# \d# \d#')
	match = pattern.compile(a)
	return match
print(Phone_number([3333, 3444,4444]))