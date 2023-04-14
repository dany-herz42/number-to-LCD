from Display import Display

def getData():
    numbers = input("Introduce un numero: ")
    width = input("Introduce el ancho: ")
    height = input("Introduce el alto: ")

    try:
        int(width)
        int(height)
        display = Display(numbers, width, height)
        display.printDisplay()
    except ValueError:
        print("Debe ingresar solo numeros naturales.")
        getData()

getData()
