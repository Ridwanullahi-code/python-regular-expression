import re 
phone_number = ("123 567 678333")
reg_pattern = re.compile(r'\b\d{3} \d{3} \d*')
search = reg_pattern.search(phone_number)
print(search)

name = ("Ridwanullahi9")
pattern = re.compile(r'[0-9]+')
search = pattern.search(name)
print(search)
