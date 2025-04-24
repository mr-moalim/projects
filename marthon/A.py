r = list(str(input("Enter six digit number: ")))
w = [int(i) for i in r]
total = 0

while True:
    total = sum(w)
    if 0 < total < 10:
        break
    else:
        w = [int(i) for i in str(total)]

print(total)
