a = 33
b = 44
if a > b:
    print ("Correct")
elif a < b: 
    print ("Not correct")
else:
    print ("Wrong")
    
# elif means ELSE IF

for numbers in range (12):
    print (numbers)
# What is happening here? numbers is a variable

for thirties in range (31, 40):
    print (thirties)
    
for odd in range (1,11, 2):
    print (odd)
    print (odd+1) #prints even numbers
    
x = 23
y = 27
while x+y <51:
    print (x+1)
    x += 5
    
    
z = 2
while z < 6:
    print (z)
    z += 1
    
#FUNCTIONS
def function_name():
    print ("Evanson")
#Calling the Function
function_name()

lName = "Mayabi" #lastname is a variable
def my_function(fName): #fName is (a variable but here it is called) an argument
    print(fName + "Mayabi") 
    print(f"{fName} Maiyami")
my_function("Evans") #the value for the variable is the parameter


def my_func(fSchool, sSchool):
    print("{} {}".format(fSchool, sSchool))
    print("We love {} and {} High Schools".format(fSchool, sSchool))
my_func("Starehe", "Maseno")

#A function that can collect user input
def my_func(fSchool):
    return("I schooled at " + fSchool) #the plus adds (concatenates) the two
    print()
greet = my_func(input("Enter Your School Name: "))
print(greet)



