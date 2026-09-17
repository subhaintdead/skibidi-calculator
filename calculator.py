# this is gonna be some calculator that gives a different answer than it should. lets see how it works (its been like a year i havent used python, and i think i may have alzheimers, let me relearn the keywords and stuff, its gonna take not much time)


def legitstuff(a, b, operator):
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


a = int(input("enter the first number: "))
operator = input("enter the operator: ")
b = int(input("enter the second number: "))

result = legitstuff(a, b, operator)
print(result)
