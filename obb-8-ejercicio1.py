def main():

    fichero = open('fichero.txt', 'w')
    fichero.write("Escribiendo \n")
    fichero.close
    
    fichero = open('fichero.txt', 'r+')
    fichero.readline()
    fichero.write('segunda linea')
    
    fichero.seek(0)
    print(fichero.read())
    fichero.close()

    

    

if __name__ == main():
    main()
    