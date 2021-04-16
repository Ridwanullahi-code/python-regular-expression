#exercise1 
#python  regular expression for valid phone number 
import re

def extract_phone(input):
 	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
 	match = phone_regex.search(input)
 	if match:
 		return match.group()
 	return None

print(extract_phone('my number is 432 567-8976'))
print(extract_phone('my number is 433 657-565775'))
print(extract_phone('454 756-5657'))
print(extract_phone('432 456-7578'))

# exercise2 
# python regular expression for valid email address
import re
def extract_email(email):
	email_pattern = re.compile(r'\b\w+@\w+\.[a-z]+')
	match = email_pattern.search(email)
	if match:
		return match.group()
	return None 

print(extract_email('ajayi@gamil.com'))
print(extract_email('olalekanridwanullahi@gamil.com'))
print(extract_email('ajayiridwanullahi01@gmail.com22'))

# exercise3 
# python regular expression for
import re
url_pattern = re.compile(r'(\w+//:)(w{3}\.\w+\.\w+)([\w:@%_\+\.~#?&//=]*)')
match = url_pattern.search('https//:www.my_website.com/bi0?data=blahdog=yes')
print(f'Protocol: {match.group(1)}')
print(f'Domain: {match.group(2)}')
print(f'Everything Else: {match.group(3)}')

# exercise4
#regular expression for Email
import re 
regex = re.compile(r"""
	^(\w+)  #first part of email
	@		#single @ sign
	(\w+)	#email provider
	\.      #single period
	(\w+)$ 	#com, org, net, etc
""", (re.VERBOSE|re.IGNORECASE))
match = regex.search('Thomas123@Yahool.com')
print(match.group())
print(match.groups())

# exercise 5
#python regular expression to search for word pattern
import re 
text = 'last night Mrs. Daisy and Mr. White murdered Ms. Cow '
pattern = re.compile(r'(Mr.|Mrs.|Ms.) [a-z]+', re.I)
result = pattern.sub('REDACTED, text')
print(result)