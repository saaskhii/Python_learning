#Q10

var1=(input("Enter first list: "))
var2=(input("Enter second list: "))
print("list 1 is:")
for x in var1:
    print(x)
print("list 2 is:")
for y in var2:
    print(y)
if len(var1)>len(var2):
    print("List 1 is big than list2")
elif len(var1)==len(var2):
    print("Both list are same")
else:
    print("list 2 is big than list 1")
