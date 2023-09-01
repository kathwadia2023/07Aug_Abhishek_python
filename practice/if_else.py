A=int(input("Enter value of A:"))
B=int(input("Enter value of B:"))

if A!=0 and B!=0:
    if A>B:
        print("SUM A + B:", A+B)
    elif A<B:
        print("SUB of A - B:", A-B)
    elif A==B:
        print("multi A*B", A*B)
else:
    print("Error")