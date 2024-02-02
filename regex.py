import re


def  main():
    print("Is passport valid: ", is_passport_valid("КМ884422"))
    print("Is inn valid: ", is_inn_number_valid("1234567894"))
    print("Is car number valid: ", is_car_number_valid("ХХ4545АА"))

def is_passport_valid(passport: str) -> bool:
    pattern = r'^[А-Я]{2}\d{6}$'
    return re.fullmatch(pattern, passport) is not None

def is_inn_number_valid(inn: str) -> bool:
    pattern = r'^\d{10}$'
    return re.fullmatch(pattern, inn) is not None

def is_car_number_valid(car_number: str) -> bool:
    pattern = r'^(РР|МІ|ХХ|ЕХ)[0-9]{4}[А-Я]{2}$'
    return re.fullmatch(pattern, car_number) is not None

if __name__ == "__main__":
    main()

