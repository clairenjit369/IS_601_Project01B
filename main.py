from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics

cal = Calculator()
stats = Statistics()

try:
    while True:
        print("Choose an option from the following:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square")
        print("6. Square Root")
        print("7. Mean")
        print("8. Median")
        print("9. Mode")
        print("10. Standard Deviation")
        print("11. Variance")

        option = int(input().strip())

        if option == 1:
            print("Enter number 1:")
            a = int(input().strip())

            print("Enter number 2:")
            b = int(input().strip())
            print("Result is", cal.add(a, b))
        elif option == 2:
            print("Enter number 1:")
            a = int(input().strip())

            print("Enter number 2:")
            b = int(input().strip())
            print("Result is", cal.subtract(a, b))
        elif option == 3:
            print("Enter number 1:")
            a = int(input().strip())

            print("Enter number 2:")
            b = int(input().strip())
            print(cal.multiply(a, b))
        elif option == 4:
            print("Enter number 1:")
            a = int(input().strip())

            print("Enter number 2:")
            b = int(input().strip())
            print("Result is", cal.divide(a, b))
        elif option == 5:
            print("Enter number 1:")
            a = int(input().strip())
            print("Result is", cal.square(a))
        elif option == 6:
            print("Enter number 1:")
            a = int(input().strip())
            print("Result is", cal.sqrt(a))
        elif option == 7:
            print("Enter number of numbers:")
            count = int(input().strip())
            data = [int(input().strip()) for i in range(count)]
            print("Result is", stats.get_mean(data))
        elif option == 8:
            print("Enter number of numbers:")
            count = int(input().strip())
            data = [int(input().strip()) for i in range(count)]
            print("Result is", stats.get_median(data))
        elif option == 9:
            print("Enter number of numbers:")
            count = int(input().strip())
            data = [int(input().strip()) for i in range(count)]
            print("Result is", stats.get_mode(data))
        elif option == 10:
            print("Enter number of numbers:")
            count = int(input().strip())
            data = [int(input().strip()) for i in range(count)]
            print("Result is", stats.get_stdev(data))
        elif option == 11:
            print("Enter number of numbers:")
            count = int(input().strip())
            data = [int(input().strip()) for i in range(count)]
            print("Result is", stats.get_variance(data))

        print("Exit :: Press 1 || Continue :: Press 0")
        exit_pressed = int(input().strip())
        if exit_pressed == 1:
            print("Bye!")
            break;
except:
    print("Invalid Literal :: Should be an Integer")


