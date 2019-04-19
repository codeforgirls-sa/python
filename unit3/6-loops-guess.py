#Create a variable called “rand” and assign it a number between 0 and 10
rand = 8
#Create a variable called “guess” and assign it -1
guess = -1
#Use while loop to iterate while "guess" is not equal to "rand"
while guess != rand:
    #Ask the user to input a number, take it as integer and store it in "guess"
    guess = int(input('Guess a number: '))
    #Print to the user “Correct”, “too low” or “too high” based on comparing the input to rand number
    if guess>rand:
        print('too high')
    if guess<rand:
        print('too low')
    if guess == rand:
        print('Correct!')
