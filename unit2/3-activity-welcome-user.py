print('Hello!')
name = input('Please, tell me what is your name?')

while name.isalpha() is False:
	print('Sorry, you can only use valid characters')
	name = input('Please, tell me what is your name?')

print("Welcome", name)