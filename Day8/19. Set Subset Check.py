"""19. Set Subset Check: Check if the fruits set is a subset of the vegetables set and print the result."""
fruit={"Watermelon","pineapple","kiwi","guava","tomato","banana"}
vegetable={"spinach","pumpkin","potato","carrot",}
x=fruit.issubset(vegetable)
if x :
    print("fruit is subset of vegetable.")
else:
    print("fruit is not a subset of vegetable")
