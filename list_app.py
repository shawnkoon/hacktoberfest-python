cars = []
num = int(input("How many cars do you want to add?\n"))

while num != 0:
	car = input("Type your car\n")
	cars.append(car)
	num -= 1

print("List of cars looks like this: ")
for car in cars:
	print(car)

