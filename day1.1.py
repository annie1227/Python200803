height=float(input("pelase enter your hight in meter:"))
weight=float(input("please enter your weight in kilograms:"))
bmi=(weight/height**2)
print ("your BMI is: ",bmi)
if bmi<18.5:
    print("體重不足")
elif bmi<24:
    print("正常")
elif bmi<27:
    print("過重")
elif bmi<30:
    print("輕度肥胖")
elif bmi<35:
    print("中度肥胖")
else:
    print("重度肥胖")
