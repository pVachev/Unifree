my_name = input('What is your name?: ')


cont = True

while(cont):
    for letter in my_name:
        print(letter)


    decision = input('Wouold you like to continue?: ')

    if decision == "n":
        cont = False
