#Topic4
#Q1

sec_no=6
var=None
while True:
    var=int(input("Guess a number:"))
    if sec_no==var:
        print("you guessed right.......")
        break
    else:
        print("Guess again!!")
