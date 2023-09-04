import random
'''
    rock + paper --> paper wins
    rock + scissor --> rock wins
    paper + scissor --> scissor wins

    rock + rock --> draw
    paper + paper --> draw
    scissor + scissor --> draw
'''
print("Enter choice \n 1.Rock \n 2.Paper \n 3.Scissor")
while True:

    ch = (input("Enter your choice :")).lower().capitalize()

    print("user choice:\t",ch)
    cc=random.choice(["Rock","Paper","Scissor"])
    print("computer choice:\t",cc)
    if cc==ch:
       print("draw")
    elif cc=="Rock":
        if ch=="Paper":
            print("user win😁")
            break
        else:
            print("computer win 😈")
    elif cc=="Paper":
        if ch=="Scissor":
            print("user win😊")
            break
        else:
            print("computer win 😈")
    else:
        if ch=="Rock":
            print("user win😊")
            break
        else:
            print("computer win 😈")

