def base(number,base):
    dec = number
    result = ""
    while dec != 0:
        dec = dec % base
        result = result + str(dec//base)
    print("The number in that base is",result)

x = int(input("Enter a number:"))
base(x,2)
    