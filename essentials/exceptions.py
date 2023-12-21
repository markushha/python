# exceptions

try:
    n1 = int(input("Enter a number to divide: "))
    n2 = int(input("Enter a number to divide by: "))

    print(n1/n2)
except ZeroDivisionError as e:
    print("You can't divide by zero", e)
except ValueError as e:
    print("Please, input numbers only", e)
except Exception as e:
    print("Something went wrong :(", e)
else:
    print("It will be executed only if no exceptions were catched")
finally:
    print("It'll be executed anyways")