with open("datosclientes.txt") as datosclientes:
    for line in datosclientes:
        print(line.strip().split("\t"))