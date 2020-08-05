score=input("please enter your score: ")
score=int(score)
if score >=0 and score <=100:
    print("you are in level:")
    if score>=90:
        print("A")
    elif score>=80:
        print("B")
    elif score>=70:
        print("C")
    elif score>=60:
        print("D")
    else:
        print("E")
else:
    print("please enter again")