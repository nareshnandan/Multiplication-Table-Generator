def multiplication_table(number):
    print(f"Multiplication Table for {number}")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# usage
number = int(input("Enter a number: "))
multiplication_table(number)