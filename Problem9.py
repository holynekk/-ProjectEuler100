a = int(input())
for i in range(a):
    anan = []
    number = int(input())
    for y in range(1,int(number/2)+1):
        if y < (number**2 - 2*number*y)/(2*number - 2*y):
            if (number ** 2 - 2 * number * y) / (2 * number - 2 * y) < number-y-(number**2 - 2*number*y)/(2*number - 2*y):
                if y**2 + ((number**2 - 2*number*y)/(2*number - 2*y))**2 == (number-y-(number**2 - 2*number*y)/(2*number - 2*y))**2:
                    anan.append((y*((number**2 - 2*number*y)/(2*number - 2*y))*(number-y-(number**2 - 2*number*y)/(2*number - 2*y))))

    if anan == []:
        print -1
    else:
        print max(anan)

