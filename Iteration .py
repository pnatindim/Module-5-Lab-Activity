#Patric Natindim
#March 5 2025

#Iterates the integers from 1 to 50

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both")
    elif num % 3 == 0:
        print("Divisible by three")
    elif num % 5 == 0:
        print("Divisible by five")
    else:
        print(num)
