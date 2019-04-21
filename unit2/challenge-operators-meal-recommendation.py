hot = True
cold = False
morning = True
evening = False
night = False

soup = False
biscuit = False
cereal = False
pizza = False

if morning:
    if cold:
        biscuit = True
    else:
        cereal = True

elif evening:
    pizza = True
    if cold:
        soup = True

elif night:
    pizza = True
    cereal = True
    if cold:
        soup = True

print("soup", soup)
print("biscuit", biscuit)
print("cereal", cereal)
print("pizza", pizza)
