def view_notes():
    choice_2 = input("Enter Name/Title to view note : ")
    f = open('E_notebook.txt', 'r')
    # print(f.read('E_notebook.txt'))
    # f.read()
    for i in f:
        if choice_2 in i:
            print(i)
       