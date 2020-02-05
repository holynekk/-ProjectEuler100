a = int(input())
for i in range(a):
    b = int(input())
    sum_squares = (2*b+1)*b*(b+1)/6
    square_sum = (b*(b+1)/2)**2
    print square_sum - sum_squares
