print("WELCOME TO CALCULATOR -Dharan" )
print("----------------------------------")
print("--------->> OPERATIONS <<----------")
print("want to add? click 1")
print("want to subtract? click 2")
print("want to multiply? click 3")
print("want to divide? click 4")
print("want to find remainder? click 5")
print("want to find power? click 6")
print("want to find prime number or not? click 7")
print("want to find factorial? click 8")
print("want find percentage? click 9")
print("want find log? click 10")
print("want to find sin? click 11")    
print("want to find cos? click 12")
print("want to find tan? click 13")
print("want to find inverse sin? click 14")
print("want to find inverse cos? click 15")
print("want to find inverse tan? click 16")
while True:
    n=int(input("Enter the number: "))
    print("--------------------------")
    if n == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("ANSWER: ",a+b)
    elif n == 2: 
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print("ANSWER: ",a-b)
    elif n == 3:
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print("ANSWER: ",a*b)
    elif n == 4:
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        if b == 0:
            print("Error: Division by zero")
        else:
            print("ANSWER: ",a/b)
    elif n == 5:
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print("ANSWER: ",a%b)
    elif n == 6:
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print("ANSWER: ",a**b)
    elif n == 7:
        a = int(input("enter number: "))
        if a == 1:
            print("no")
        else:
            for i in range(2,a):
                if a % i == 0:
                    print("ANSWER: ","no")     

                else:
                    print("ANSWER: ","yes")
    elif n == "8":
        a = int(input("enter number: "))
        for i in range(a,0,-1):
            a = a*i
        print("ANSWER: ",a)
    elif n == "9":
        a = int(input("enter number: "))
        b = int(input("enter total number: "))
        print("ANSWER: ",(a/b)*100)
    elif n == "10":
        import math
        a = int(input("enter number: "))
        b = int(input("enter base: "))
        print("ANSWER: ",math.log(a,b))
    elif n == "11":
        import math
        a = int(input("enter number: "))
        print("ANSWER: ",math.sin(a))
    elif n == "12":
        import math
        a = int(input("enter number: "))
        print("ANSWER: ",math.cos(a))
    elif n == "13":
        import math
        a = int(input("enter number: "))
        print("ANSWER: ",math.tan(a))
    elif n == "14":
        import math
        a = int(input("enter number: "))
        print("ANSWER: ",math.asin(a))
    elif n == "15":
        import math
        a = int(input("enter number: "))
        print("ANSWER: ",math.acos(a))
    elif n == "16":
        import math
        a = int(input("enter number: "))
        print("ANSWER: ",math.atan(a))
    else:
        print("Invalid input")
    a=input("Do more operations? (y/n): ")
    if a == "n":
        break
    else:
        continue

