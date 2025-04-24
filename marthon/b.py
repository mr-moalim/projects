n = int(input("how much times you want to try? "))
for i in range(n):
    r = float(input("Enter the radius:"))
    l = float(input("Enter the length:"))
    w = float(input("Enter the width:"))
    circle = 2 * 3.14 * r * r
    rect = l * w
    if circle > rect :
        print("yes")
    elif circle == rect :
        print("same")
    else:
        print("no")