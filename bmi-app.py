# Write a program that calculates Body Mass Index of individuals
# Itialize name, weight and height 
myName = ""
height = float
weight = float
#prompt the user to entre their name
myName = str(input("Your name: " + myName ))
height = float(input( "Height: " ))
weight = float(input( "Weight: " ))
# intialize BMI calculator
bmi = weight / ( height **2 )     
if bmi > 25:
     print( myName + " Is Obes since the BMI is: ", bmi )
else:
     if bmi <= 25:
          print( myName + " Is normal since the BMI is: ", bmi )
     