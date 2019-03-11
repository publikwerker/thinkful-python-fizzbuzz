n = 100
counter = 0
print("Fizz buzz counting up to %!", n)
while counter != n:
    counter+=1
    if counter % 15 == 0:
        print("fizz buzz")
    elif counter % 3 == 0:
        print("fizz")
    elif counter % 5 == 0:
        print("buzz")
    else: print(counter)