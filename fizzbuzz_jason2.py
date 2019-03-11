import sys
n = False
print("User supplied {} arguments at run time".format(len(sys.argv)))

for arg in sys.argv[0:]:
  print(arg)

if len(sys.argv) == 2:
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("entry must be a positive integer")

while type(n) != int:
    try:
        n = int(input("Enter a value for the Fizz Buzz game example."))
    except ValueError:
        print("entry must be a positive integer")
counter = 0
print("Fizz buzz counting up to {}!".format(n))
while counter < n:
    counter+=1
    if counter % 15 == 0:
        print("fizz buzz")
    elif counter % 3 == 0:
        print("fizz")
    elif counter % 5 == 0:
        print("buzz")
    else: print(counter)