
print("Hello Welcome This is Simple Calculator")

num1 = 0.00
num2 = 0.00
space = "--------------------------------------------------------------------"
def Takeinput():
    global num1 , num2
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))


def AddNum():
    print("Addition of 2 Numbers:")
    Takeinput()
    print(f"{num1} + {num2} = {num1+num2}")
    print(space)

def SubNum():
    print("Substration of 2 Number:")
    Takeinput()
    print(f"{num1} - {num2} = {num1-num2}")
    print(space)

def MulNum():
    print("Multiplication of 2 Number:")
    Takeinput()
    print(f"{num1} * {num2} = {num1*num2}")   
    print(space) 

def DivNum():
    print("Devision of 2 Number:")
    Takeinput()
    print(f"{num1} / {num2} = {num1/num2}")
    print(space)



while True:
    task = input("""
    Task:
    1. Add (Press +)
    2. Subtract (Press -)
    3. Multiply (Press *)
    4. Divide (Press /)
    5. Exit (Press x)
    Please Select You Task: """)

    match task :
        case "+": AddNum()
        case "-": SubNum()
        case "*": MulNum()
        case "/": DivNum()
        case "x": break
        case _: print("Invalid Input"); print(space)





