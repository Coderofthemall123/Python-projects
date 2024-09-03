x = int(input("Enter lower range: "))
y = int(input("Enter higher range: "))
def square(low, high):
    count = 0
    while count**2 < low:
        count += 1
    odd_squares = []
    even_squares = []
    while count**2 >= low and count**2 <=high:
        if count**2 % 2 == 0: 
            even_squares.append(str(count**2))
        else:  
            odd_squares.append(str(count**2))
        count += 1
    return odd_squares, even_squares
odd_squares, even_squares = square(x, y) 
print("Odd Squares:", odd_squares)
print("Even Squares:", even_squares)




