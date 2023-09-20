import function_generate
import view_notes 

# ++++++++++++++++++++ welcome statement   +++++++++++++++++++


Y_or_N = 'Y'
print("Welcome to Python E - Note")

print('\n')
print("Press 1 for generate Note")
print("Press 2 to view Note")
print("press 4 to exit!")
print("\n")

# choice_1 = int(input("Enter your choice :"))

while Y_or_N != 'N':
    choice_1 = int(input("Enter your choice :"))
    if choice_1 ==1:
        print("Generate")
        function_generate.gene_notes()

    elif choice_1==2:
        print("View notes...")
        view_notes.view_notes()

    elif choice_1==4:
        print("Your choice is exit!!!")
        Y_or_N = 'N'
        quit()
    else:
        print("Wrong Input.....Restart Console!!!!!!!!")


    Y_or_N = (input("Repeat the loop? Y for yes and N for Quit : ")).capitalize()
    if Y_or_N =='Y':
        print('\n')
        print("Press 1 for generate Note")
        print("Press 2 to view Note")
        print("press 4 to exit!")
        print("\n")
    else:
        print("Your choice is exit!!!")
        exit()
