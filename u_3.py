
while 1:
    subor = open("uloha3/" + input("Zadaj meno suboru: ") + ".txt", "w")

    running = True
    while running:
        subor.write(input("Zadaj vnutro suboru: ") + "\n")

        if input("chceš ešte dalej pisať? y/n  ") == "n":
            running = False
    subor.close()

    if input("Plné ukončenie? y/n  ") == "y":
        break

    

    
