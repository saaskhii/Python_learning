#Q10
var1=int(input("Enter age of person 1: "))
var2=int(input("Enter age of person 2: "))
diff= var1-var2
age_diff=abs(diff)
print("Age difference between them is:",age_diff)
if var1>var2:
    print("Person 1 is older by",age_diff,"yrs")
else:
    print("Person 2 is older by",age_diff,"yrs")
