forenames = ['Homer', 'Marge', 'Lisa', 'Bart', 'Maggie']
surname='Simplson'

fullnames=[]
for name in forenames:
    fullnames.append( name + ' ' + surname)

for name in fullnames:
    print(name)  