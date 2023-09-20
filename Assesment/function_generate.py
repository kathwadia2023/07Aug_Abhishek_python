import datetime

date_time= datetime.datetime.now()

def gene_notes():
    E_note_name = input("Enter E-note Generator Name : ")
    
    while E_note_name.isnumeric():
        print("Error : Invalid Input")
        E_note_name = input("Enter E-note Generator Name : ")

    E_note_title = input("Enter E-note Generator Title : ")

    while E_note_title.isnumeric():
        print("Error : Invalid Input")
        E_note_title = input("Enter E-note Generator Title : ")

    E_note_content = input("Enter E-note Generator Content : ")
    while E_note_content.isnumeric():
        print("Error : Invalid Input")
        E_note_content = input("Enter E-note Generator Content : ")
    
    

# +++++ File open and write code ++++++++++++
    with open('E_notebook.txt', 'a') as data_file:
        data_file.write("-------------------------------------------------\n")
        data_file.write(f"Date & Time:{date_time}\n")
        data_file.write(f"E-note Title: {E_note_title}\n")
        data_file.write(f"E-note Discription: {E_note_content}\n")
        data_file.write(f"           Note Generator: {E_note_name}\n")
  
    # data_file.close()
# gene_notes()