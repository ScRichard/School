
temp = open("uloha2/mesta.txt", "r")
mesta = temp.read().split("\n")
temp.close()


for file in mesta:
    subor = open(f"uloha2/mesto_{file}.txt", "w+")

    subor.write(f"Ahoj, toto je mesto {file}")

    subor.close()
