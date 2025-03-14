# This app will calculate BMI of individuals
# Itialize name, weight and height
myName = "Charle Otugeh"
height = 5.56
weight = 63.5

# intialize BMI calculator
bmi = weight / (height **2)
if bmi >= 30:
     print(myName + " Is Obes")
else:
     if bmi <= 25:
          print(myName + " Is normal")
     