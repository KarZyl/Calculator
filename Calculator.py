
import logging
logging.basicConfig(level=logging.INFO)


a = (input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

try: int(a)
except ValueError:
    logging.error(" Błąd! Podana wartość nie jest liczbą")

a = int(a)

number1 = input("Podaj składnik 1: " )
try: int(number1)
except ValueError:
    logging.error(" Błąd! Podana wartość nie jest liczbą")
number1 = int(number1)

number2 = input("Podaj składnik 2: " )
try: int(number2)
except ValueError:
    logging.error(" Błąd! Podana wartość nie jest liczbą")
number2 = int(number2)

if a == 1:
    answer = input("Czy chcesz dodać więcej liczb? T/N ")
    numbers = [number1, number2]
    result = number1 + number2
    while answer == "T":
        number3 = input("Podaj kolejny składnik")
        try: int(number3)
        except ValueError:
            logging.error(" Błąd! Podana wartość nie jest liczbą")
        number3 = int(number3)
        result = result + number3
        numbers = numbers + [number3]
        answer = input("Czy chcesz dodać więcej liczb? T/N ")

    logging.info(f" Dodaję liczby: {numbers}")
elif a == 2:
    result = number1 - number2
    logging.info(f" Odejmuję {number2} od {number1}")
elif a == 3:
    answer = input("Czy chcesz pomnożyć więcej liczb? T/N")
    numbers = [number1, number2]
    result = number1 * number2
    while answer == "T":
        number3 = input("Podaj kolejny składnik")
        try: int(number3)
        except ValueError:
            logging.error(" Błąd! Podana wartość nie jest liczbą")
        number3 = int(number3)
        result = result * number3
        numbers = numbers + [number3]
        answer = input("Czy chcesz pomnożyć więcej liczb? T/N")
    logging.info(f" Mnożę liczby: {numbers}")
elif a == 4:
    result = number1 / number2
    logging.info(f" Dzielę {number1} przez {number2}")
else:
    result = None
    print("Nie ma takiego działania")

print(f"Wynik to {result}")