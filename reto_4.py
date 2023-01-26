#utiliza las palabras clave try, except y rise ara elevar un error si el usuario intresa un numero negativo
# en nuestro programa de divisores



def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        if num < 0:
            raise ValueError ("No se aceptan  numeros negativos")
        print(divisors(num))
        print("Terminó mi programa")

    except (ve,ValueError):
        print("No se aceptan  numeros negativos")
        return False

    except ValueError:
        print("Debes ingresar un número")










if __name__ == '__main__':
    run()
