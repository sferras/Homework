def evenorodd():
    parameter = 2
    print("Enter a number: ")
    num1 = int(input())
    num2 = num1 + parameter
    if (num2 % 2) == 0:
        print(num1, "is even")
    else:
        print(num1, "is odd")
evenorodd()