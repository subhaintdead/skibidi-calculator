import math


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
        return None


# now the skibidi calculation
def skibidi(a, b):
    banana = a * math.pi + math.sqrt(2)
    wave = math.sin(banana) * math.cos(banana * math.sqrt(3))  # i hate trigonometry
    return wave


def skibidimath(a, b, operator, legitnum):

    # rizz time
    rizz = (
        skibidi(a, b) * 6.8
    )  # ig the number might be too small otherwise, or even if it is a lil too big, doesnt matter

    if operator == "+":
        skibidinum = legitnum + rizz
    elif operator == "-":
        skibidinum = legitnum - rizz
    elif operator == "/":
        skibidinum = legitnum + (rizz / 4)
    elif operator == "*":
        skibidinum = legitnum + (rizz * 2)
    else:
        skibidinum = legitnum
    return skibidinum


banner = r""""

 ____   _     _  _      _      _  _                     
/ ___| | | __(_)| |__  (_)  __| |(_)                    
\___ \ | |/ /| || '_ \ | | / _` || |                    
 ___) ||   < | || |_) || || (_| || |                    
|____/ |_|\_\|_||_.__/ |_| \__,_||_|                    
  ____        _               _         _               
 / ___| __ _ | |  ___  _   _ | |  __ _ | |_  ___   _ __ 
| |    / _` || | / __|| | | || | / _` || __|/ _ \ | '__|
| |___| (_| || || (__ | |_| || || (_| || |_| (_) || |   
 \____|\__,_||_| \___| \__,_||_| \__,_| \__|\___/ |_|   

"""

version = "v2.0.0"


print(banner)
print(f"skibidi calculator {version}, the least accurate arithmetic calculator")
print("=" * 60)


a = int(input("enter the first number: "))
operator = input("enter the operator: ")
b = int(input("enter the second number: "))

print("-" * 60)

if operator not in ["+", "-", "*", "/"]:
    print("invalid operator")
else:
    legitnum = legit(a, b, operator)

    if operator == "/" and b == 0:
        print("bro you cant divide by 0(even the fakest clculator has limits gng)")
    else:
        skibidinum = skibidimath(a, b, operator, legitnum)
        skibidinum = round(skibidinum, 2)
        if skibidinum == legitnum:
            skibidinum += 1  # edge case
        print(f"the answer is: {skibidinum}")
        print("run successfully. run again for some more brain-smoothening math")

print("=" * 60)
