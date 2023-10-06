"""14. Set Difference: Find and print the items that are in the fruits set but not in the
vegetables set.
"""

set1={"Sakshi",24,"sakshig30820@gmail.com","Mumbai","Female"}
set2={"Mansi",24,"mansip2911@gmail.com","Mumbai", "Female"}
union1=set1.difference(set2)
union2=set2.difference(set1)

print(union1,union2)
