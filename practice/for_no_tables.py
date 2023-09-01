Number_of_tables = int(input("How many number of tables you want to print!?"))

for a in range(0,Number_of_tables):
    n=int(input(f"enter table {a} value:"))

    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

