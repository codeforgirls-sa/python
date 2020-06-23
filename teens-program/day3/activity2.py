weekend = True
test_sunday = False

if (weekend == True and test_sunday == False):
    print('We will go out.')
elif (weekend != True or test_sunday != False):
    print('We will not go out.')

# Extra
# if (weekend == True and test_sunday == False):
#     print('We will go out.')
# elif (weekend != True and test_sunday == False):
#     print('We will not go out; it is not the weekend.')
# elif (weekend == True and test_sunday != False):
#     print('We will not go out; you have a test on sunday.')
# else:
#     print('We will not go out; it is not the weekend and you have a test on sunday.')