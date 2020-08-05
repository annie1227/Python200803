english=int(input("請輸入英文成績: "))
math=int(input("請輸入數學成績: "))
if english>=90 and math>=90:
    print("great job!")
elif english<60 and math<60:
    print("there's a punishment")
elif english<60 or math<60:
    print("work harder!")
else:
    print("keep going!")