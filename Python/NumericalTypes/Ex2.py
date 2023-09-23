
```
# We are asked to create a program to calculate 
# average score for a student with the exam scores following:
# 1 -> 70
# 2 -> 95
# 3 -> 50 
# 4 -> 45
# Calculate the average score for the student 
# and print the average in following format. 
# Average score for given student grades is `avgScore`.


exam1 = 70
exam2 = 95
exam3 = 50
exam4 = 45

number_of_exams= 4
sum = exam1 + exam2 + exam3 + exam4
avg = sum/ number_of_exams

print(avg)

print("avarage score for given student grades is" , avg)

#What is the type of a variable avg?
#Float
#type() function
#When we put the variable name in a type function it will 
# show the type of a variable. 
print(type(avg))
