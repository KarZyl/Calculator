
import logging
logging.basicConfig(level=logging.INFO)

print(type(3.1))

print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

def input_try_int():
    argument = input()
    check = 0
    while check == 0:
        try: 
            int(argument)
            check = 1
            argument = int(argument)
        except ValueError:
            try:
                float(argument)
                check = 1
                argument = float(argument)
            except ValueError:
                check = 0
                logging.error(" Błąd! Podana wartość nie jest liczbą")
                argument = input("podaj nową wartość: ")
    return argument

operation = input_try_int()

while operation != 1 and operation !=2 and operation !=3 and operation !=4:
    print("Wybrano nieprawidłowe działanie, wybierz spośród liczb 1-4: ")
    operation = input_try_int()

print("Podaj składnik 1: ")

number1 = input_try_int()

print("Podaj składnik 2: ")

number2 = input_try_int()

if operation == 1:
    answer = input("Wprowadź 'T' jeśli chcesz dodać więcej liczb: ")
    numbers = [number1, number2]
    result = number1 + number2
    while answer == "T":
        print("Podaj kolejny składnik")
        number3 = input_try_int()
        result = result + number3
        numbers = numbers + [number3]
        answer = input("Wprowadź 'T' jeśli chcesz dodać więcej liczb: ")

    logging.info(f" Dodaję liczby: {numbers}")
elif operation == 2:
    result = number1 - number2
    logging.info(f" Odejmuję {number2} od {number1}")
elif operation == 3:
    answer = input("Wprowadź 'T' jeśli chcesz pomnożyć więcej liczb: ")
    numbers = [number1, number2]
    result = number1 * number2
    while answer == "T":
        print("Podaj kolejny składnik")
        number3 = input_try_int()
        result = result * number3
        answer = input("Wprowadź 'T' jeśli chcesz pomnożyć więcej liczb: ")
    logging.info(f" Mnożę liczby: {numbers}")
elif operation == 4:
    result = number1 / number2
    logging.info(f" Dzielę {number1} przez {number2}")
else:
    None

print(f"Wynik to {result}")
