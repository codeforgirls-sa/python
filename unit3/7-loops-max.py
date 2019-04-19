#Create a list of positive numbers called "nums"
nums = [1,3,10,2]
#Create a variable called "max_value" and assign it -1
max_value = -1
#Iterate for each number in the "nums" list
for number in nums:
    #If number is greater than "max_value", make "max_value" equals to the number
    if number > max_value: 
        max_value = number
#Print the maximum value       
print(max_value)