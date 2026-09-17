# this is gonna be some calculator that gives a different answer than it should using some gibberish formula


def legit(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "gng u cant divide by 0"
        else:
            return a / b
    else:
        return "gng that aint a operator"


# now the skibidi calculation


def dsum(n):  # digits sum, in case i forget it later
    total = 0
    for banana in str(int(n)):
        total += int(banana)
    return total


def skibidimath(a, b, operator, legitnum):

    # rizz time

    rizz = (
        dsum(a) * 6.8 + dsum(b) * 3 - 6.7
    ) % 13  # 6.8 specifically cuz 68 is the number between six-seven and 69 divided by 10

    if operator == "+":
        skibidinum = legitnum + rizz - 5
    elif operator == "-":
        skibidinum = legitnum - rizz + 3
    elif operator == "/":
        skibidinum = legitnum + (rizz / 4) + 1.5
    elif operator == "*":
        skibidinum = legitnum + (rizz * 4) - 2
    else:
        skibidinum = legitnum
    return skibidinum


a = int(input("enter the first number: "))
operator = input("enter the operator: ")
b = int(input("enter the second number: "))

if operator not in ["+", "-", "*", "/"]:
    print("invalid operator")

legitnum = legit(a, b, operator)

skibidinum = skibidimath(a, b, operator, legitnum)
skibidinum = round(skibidinum, 2)
if skibidinum == legitnum:
    skibidinum += 1
print(skibidinum)
