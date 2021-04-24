
def product(a, b):
    return a * b

def total(a, b):
    return a + b

def totaldp(a, b, c):
    return a + b + c

def deduction(a, b):
    return a - b

def main():
    print("Payroll Program As of April 16, 2021")
    print("----------------------\n    EMPLOYEE INFO\n----------------------")
    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    dp = input("Enter Department: ")
    pt = input("Enter Position: ")
    print("----------------------\n    BASIC PAY\n----------------------")
    dw = int(input("Enter number of days work: "))
    rpd = int(input("Enter Rate Per Day: "))
    print("----------------------\n    OVERTIME PAY\n----------------------")
    nh = int(input("Enter number of Hours: "))
    rph = int(input("Enter Rate Per Hour: "))
    print("----------------------\n    DEDUCTIONS PAY\n----------------------")
    sss = int(input("Enter SSS: "))
    pi = int(input("Enter Pag-ibi: "))
    late = int(input("Enter Late: "))
    print("----------------------\n    SUMMARY \n----------------------")
    print(f"Employee Name: {name}")
    print(f"Employee Number: {number}")
    print(f"Department: {dp}")
    print(f"Position: {pt}")
    print(f"Total Basic Pay: {product(dw, rpd)}")
    print(f"Total Overtime Pay: {product(nh, rph)}")
    print(f"Grosspay: {total(product(dw, rpd), product(nh, rph))}")
    print(f"Total Deduction: {totaldp(sss, pi, late)}")
    print(f"Net Pay: {deduction(total(product(dw, rpd), product(nh, rph)), totaldp(sss, pi, late))}")

while 1:
    main()
    op = input("Another one Y/N: ")
    if op == 'y' or op == 'Y':
        continue
    elif op == 'n' or op == 'N':
        break
    else:
        print("Wrong Choice")
        break

