print("Please input a string of random letters")
answer = input()
maxlength = 0
current = answer[0]
longest = answer[0]

for i in range(len(answer) - 1):
    if answer[i + 1] >= answer[i]:
        current += answer[i + 1]
        if len(current) > maxlength:
            maxlength = len(current)
            longest = current
    else:
        current = answer[i + 1]
    i += 1
print("Longest substring in alphabetical order is: " + longest)