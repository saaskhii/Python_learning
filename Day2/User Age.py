#Q4
import datetime
var1=float(input("Enter you birth year:"))
today=datetime.date.today()
year=today.year
age=year-var1
print("Your age is: ",age)
