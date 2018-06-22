n = float(input("what is your height?"))
a = float (input("what is your weight?"))
bmi= float(a/n**2)
print ("BMI=",bmi)
if bmi<16:
    print("Severely underweight")
elif 16<bmi<25:
    print("Underweight")
elif 18.5<bmi<25:
    print("Normal")
elif 25<bmi<30:
    print("Overweight")
else:
    print ("Obese")