a = b = c = 0

read_line = input("Give me 3 numbers separated by , and space (like this example): 5.1, 4, 7 ")
read_line = read_line.replace(",", "")
list_num = read_line.split()
if len(list_num) != 3:
    print("That is not 3 numbers")
    exit()
print(list_num)

try:
    a = float(list_num[0])
    b = float(list_num[1])
    c = float(list_num[2])

except ValueError:
    print("Not all are valid numbers")
    exit()

except:
    print("Some other error")
    exit()


if a >= b and a >= c:
    max = a
    min1 = b
    min2 = c
elif b >= a and b >= c:
    max = b
    min1 = a
    min2 = c
else:
    max = c
    min1 = a
    min2 = b

if max > min1 + min2:
    print("Can not form a triangle")
elif max == min1 and max == min2:
    print("equilateral ")
elif max == min1 or max == min2 or min1 == min2:
    print("isosceles")
if max*max == min1*min1 + min2*min2:
    print("Right")
elif max*max > min1*min1 + min2*min2:
    print("Obtuse")
else:
    print("Acute")

p=(a+b+c)/2
A=(p*(p-a)*(p-b)*(p-c))**(1/2)
print("The surface of the triangle is of: ", A, "square units")
