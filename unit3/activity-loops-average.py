#Create a list called "age" that contains the ages of the students of this class. 
age = [18,20,22,25,25]
#Create a variable called “sum” and assign it 0
sum = 0
#Iterate for each item in the "age" list
for item in age:
    #Add item to the sum
    sum = sum + item
#Print the average of ages by dividing "sum" to the number of students
print (sum/len(age))