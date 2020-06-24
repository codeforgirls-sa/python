grade = input('How much did you score for the test?')

if int(grade) >= 60:
    print('Congrats, you succeed!')
else:
    print('Sorry, you failed')

# is_valid = False
#
# while is_valid is False:
#     grade = input('How much did you score for the test?')
#     try:
#         if int(grade) >= 0 and int(grade) <= 100:
#             is_valid = True
#         else:
#             print('Please enter a valid number')
#     except:
#         print('Please enter a valid number')
#
#
# if int(grade) >= 60:
#     print('Congrats, you succeed!')
# else:
#     print('Sorry, you failed')