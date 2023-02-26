
import logging
logging.basicConfig(level=logging.INFO)
check = 0

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
while check == 0:
    try: 
        int(operation)
        check = 1
    except ValueError:
        check = 0
        logging.error(" Błąd! Podana wartość nie jest liczbą")
        operation = input("podaj nową wartość: ")
operation = int(operation)
check = 0

number1 = input("Podaj składnik 1: " )
while check == 0:
    try: 
        int(number1)
        check = 1
    except ValueError:
        check = 0
        logging.error(" Błąd! Podana wartość nie jest liczbą")
        number1 = input("podaj nową wartość: ")
number1 = int(number1)
check = 0

number2 = input("Podaj składnik 2: " )
while check == 0:
    try: 
        int(number2)
        check = 1
    except ValueError:
        check = 0
        logging.error(" Błąd! Podana wartość nie jest liczbą")
        number2 = input("podaj nową wartość: ")
number2 = int(number2)
check = 0

if operation == 1:
    answer = input("Czy chcesz dodać więcej liczb? T/N ")
    numbers = [number1, number2]
    result = number1 + number2
    while answer == "T":
        number3 = input("Podaj kolejny składnik")
        while check == 0:
            try: 
                int(number3)
                check = 1
            except ValueError:
                logging.error(" Błąd! Podana wartość nie jest liczbą, podaj wartość liczbową")
                check = 0
                number3 = input("podaj nową wartość: ")
        check = 0
        number3 = int(number3)

        result = result + number3
        numbers = numbers + [number3]
        answer = input("Czy chcesz dodać więcej liczb? T/N ")

    logging.info(f" Dodaję liczby: {numbers}")
elif operation == 2:
    result = number1 - number2
    logging.info(f" Odejmuję {number2} od {number1}")
elif operation == 3:
    answer = input("Czy chcesz pomnożyć więcej liczb? T/N")
    numbers = [number1, number2]
    result = number1 * number2
    while answer == "T":
        number3 = input("Podaj kolejny składnik")
        while check == 0:
            try: 
                int(number3)
                check = 1
            except ValueError:
                logging.error(" Błąd! Podana wartość nie jest liczbą")
                check = 0
                number3 = input("podaj nową wartość: ")
        check = 0
        number3 = int(number3)

        result = result * number3
        numbers = numbers + [number3]
        answer = input("Czy chcesz pomnożyć więcej liczb? T/N")
    logging.info(f" Mnożę liczby: {numbers}")
elif operation == 4:
    result = number1 / number2
    logging.info(f" Dzielę {number1} przez {number2}")
else:
    result = None
    print("Nie ma takiego działania")

print(f"Wynik to {result}")
