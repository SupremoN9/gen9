import random
import time

def luhn(card_number):
    digits = [int(x) for x in str(card_number)]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total_sum = sum(odd_digits) + sum([sum(divmod(2 * digit, 10)) for digit in even_digits])
    return total_sum % 10 == 0


def generate_card(bin_num, expiration_date=None, cvv=None):
    card_number = str(bin_num)
    while len(card_number) < 15:
        card_number += str(random.randint(0, 9))

    check_digit = str((10 - sum([int(x) for x in card_number[-1::-2]]) * 2) % 10)
    card_number += check_digit

    if expiration_date is None:
        expiration_month = str(random.randint(1, 12)).zfill(2)
        expiration_year = str(random.randint(2022, 2031))
        expiration_date = f"{expiration_month}/{expiration_year[-2:]}"
    if cvv is None:
        cvv_length = 4 if str(bin_num)[0] == '3' else 3
        cvv = str(random.randint(0, 10**cvv_length - 1)).zfill(cvv_length)

    card_info = {
        "card_number": card_number,
        "bin": str(bin_num)
    }

    if expiration_date:
        card_info["expiration_date"] = expiration_date
    else:
        expiration_month = str(random.randint(1, 12)).zfill(2)
        expiration_year = str(random.randint(2022, 2031))
        card_info["expiration_date"] = f"{expiration_month}/{expiration_year[-2:]}"

    if cvv:
        card_info["cvv"] = cvv
    else:
        cvv_length = 4 if str(bin_num)[0] == '3' else 3
        card_info["cvv"] = str(random.randint(0, 10**cvv_length - 1)).zfill(cvv_length)

    return card_info if luhn(card_number) else generate_card(bin_num, expiration_date, cvv)




from colorama import Fore

print(Fore.BLUE + "N9")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╱╭┳━━━╮")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╰╮┃┃╭━╮┃")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "┃╰━━┳╮╭┳━━┳━┳━━┳╮╭┳━━┫╭╮╰╯┃╰━╯┃")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "╰━━╮┃┃┃┃╭╮┃╭┫┃━┫╰╯┃╭╮┃┃╰╮┃┣━━╮┃")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "┃╰━╯┃╰╯┃╰╯┃┃┃┃━┫┃┃┃╰╯┃┃╱┃┃┣━━╯┃")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "╰━━━┻━━┫╭━┻╯╰━━┻┻┻┻━━┻╯╱╰━┻━━━╯")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "╱╱╱╱╱╱╱┃┃")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "╱╱╱╱╱╱╱╰╯")


bin_num = input("Ingrese el BIN: ")
expiration_date = input("¿Desea especificar la fecha de expiración? (S/N): ")
cvv = input("¿Desea especificar el CVV? (S/N): ")

if expiration_date.upper() == "S":
    expiration_date = input("Ingrese la fecha de expiración (MM/YY): ")
else:
    expiration_date = None

if cvv.upper() == "S":
    cvv = input("Ingrese el CVV: ")
else:
    cvv = None

card = generate_card(bin_num, expiration_date, cvv)
print(f'Tarjeta generada:\nNúmero de tarjeta: {card["card_number"]}\nFecha de expiración: {card["expiration_date"]}\nCVV: {card["cvv"]}\nBIN: {card["bin"]}')
