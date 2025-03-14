# Write a program that calculates Body Mass Index of individuals
# Itialize name, weight and height 
myName = ""
height = float
weight = float
#prompt the user to entre their data
myName = str(input("Your name: " + myName ))
height = float(input( "Height: " ))
weight = float(input( "Weight: " ))
# intialize BMI calculator
bmi = weight / ( height **2 )     
# use tenary opperator
message = myName + f" Is Obes since the BMI is: {bmi}" if bmi <= 25 else myName + f" Is normal since the BMI is: {bmi}"
print(message)
     