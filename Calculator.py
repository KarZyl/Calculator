import logging
logging.basicConfig(level=logging.INFO)

def validate(argument):
    try:
        argument = float(argument)
        return argument
    except ValueError:
        return False
        
def get_operation():
    while True:
        operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
        if operation in ["1", "2", "3", "4"]:
            return operation
        
def get_arguments():
    while True:
        arg = input()
        if validate(arg):
            break
    return float(arg)
 
def add(arg1, arg2):
    answer = input("Wprowadź 'T' jeśli chcesz dodać więcej liczb: ")
    numbers = [arg1, arg2]
    result = arg1 + arg2
    while answer == "T":
        print("Podaj kolejny argument")
        arg3 = get_arguments()
        result = result + arg3
        numbers = numbers + [arg3]
        answer = input("Wprowadź 'T' jeśli chcesz dodać więcej liczb: ")
    logging.info(f" Dodaję liczby: {numbers}")
    return result

def sub(arg1, arg2):
    result = arg1 - arg2
    logging.info(f" Odejmuję {arg2} od {arg1}")
    return result

def mul(arg1, arg2):
    answer = input("Wprowadź 'T' jeśli chcesz pomnożyć więcej liczb: ")
    numbers = [arg1, arg2]
    result = arg1 * arg2
    while answer == "T":
        print("Podaj kolejny argument")
        arg3 = get_arguments()
        result = result * arg3
        numbers = numbers + [arg3]
        answer = input("Wprowadź 'T' jeśli chcesz pomnożyć więcej liczb: ")
    logging.info(f" Mnożę liczby: {numbers}")
    return result

def div(arg1, arg2):
    result = arg1 / arg2
    logging.info(f" Dzielę {arg1} przez {arg2}")
    return result

if __name__ == "__main__":
    operation = get_operation()
    print("Podaj pierwszy argument: ")
    arg1 = get_arguments()
    print("Podaj drugi argument: ")
    arg2 = get_arguments()
    print(arg1, arg2, operation)
    if operation == "1":
        print("Wynik to: ",add(arg1, arg2))
    elif operation == "2":
        print("Wynik to: ",sub(arg1, arg2))
    elif  operation == "3":
        print("Wynik to: ",mul(arg1, arg2))
    elif  operation == "4":
        print("Wynik to: ",div(arg1, arg2)) 
