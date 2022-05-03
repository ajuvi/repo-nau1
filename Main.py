from Nau import Nau

def menu():
    print("w- Moure dreta")
    print("a- Moure equerre")
    print("d- Moure amunt")
    print("s- Moure moure avall")    
    print("0- Sortir")

def main():

    menu()
    
    nau = Nau(0,0)

    sortir=False
    while not sortir:
        op = input('Entra una opció')
        if op=='d':
            print('moure a la dreta')
        elif op=='a':
            print('moure a l''esquerre')
        elif op=='w':
            print('moure a amunt')
        elif op=='s':
            print('moure a avall')
        elif op=='0':
            sortir=True
            print("Has sortit de l'avió")
        
if __name__ == "__main__":
    main()
