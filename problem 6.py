a = int(input("Enter Your Marks : "))

# Here i did a mistake that was i forgot that there is a function called elif also.
# For every if and elif you don't need else function to be added
# Don't write print function for every if and elif funciton.if you do so, in the result you will get 
# it printed for every function.


if 90 < a <= 100:
    grade = "EXCELLENT"

elif 80< a <=90 :
    grade = "A"
 

elif 70<a<=80 :
    grade = "B"


elif 60<a<=70 :
    grade = "C"


elif 50<a<=60 :
    grade = "D"


elif a<=50 :
    grade = "Fail hai nalle tu"



elif a>100 :
    grade = "ENTER A VALID NUMBER"     


print("Your grade is : " , grade)


