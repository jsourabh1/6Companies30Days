def solve(N):

    # // the number of squares will be(N*(N+1)*((2*N)+1))/6
    print(f'The number of squares in {N}*{N} chessboard is {(N*(N+1)*((2*N)+1))/6}')
    return 


for _ in range(int(input("Enter the no of test cases"))):

    solve(int(input("Enter the size of the chessboard")))