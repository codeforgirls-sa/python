soup = False
biscuit = False
cereal = False
pizza = False

weather = ""
time = ""

while not time or not weather: # i.e. they're blank
    weather = input("Is it hot or cold?")
    time = input("What time is it? morning, evening, or night?")

if time == "morning":
    if weather == "cold":
        biscuit = True
    else:
        cereal = True

elif time == "evening":
    pizza = True
    if weather == "cold":
        soup = True

elif time == "night":
    pizza = True
    cereal = True
    if weather == "cold":
        soup = True

print("soup", soup)
print("biscuit", biscuit)
print("cereal", cereal)
print("pizza", pizza)
