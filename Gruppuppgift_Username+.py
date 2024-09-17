import pyinputplus as py
import datetime
from datetime import datetime, date


# 3 funktioner
# minst 3 kommentarer
# list dict eller tuple

# username
# Epost
# födelsedatum
# ålder 
# telefon
# nyhetsbrev
# färg med alternartiv


username:str = py.inputStr('Ange ett användarnamn: ')
print (f"Välkommen {username}!")

epost:str = py.inputEmail('\nAnge din epost adress: ')
print ('Epost godkänd. ') 

birthday:int = py.inputDate('\nAnge din födelse dag. (MM/DD/ÅÅÅÅ): ')
# print (((age) - (birthday)).days // 365) (test) ger ålder i år

def calculate_age(birthday: date) -> int:
    difference = datetime.now().date() - birthday
    age: int = int(difference.days // 365)
    return age
# Funktion för att räkna ut ålder

def check_age(age: int) -> bool:
    if age < 18:
        print("Du är för ung! Du måste vara 18.")
        return False
    
    elif age > 100:
        print("Du är för gammal och vis!")
        return False
    
    else:
        print(f'Du är {age} år gammal.')
        return True
#funktion för att kolla om åldern är över 18 och under 100


def check_number(phone_number) -> bool:
    if valid_telenum(phone_number):
        print("Telefonnumret är giltigt.")
        return True
    else:
        print("Ogiltigt telefonnummer. Det måste vara exakt 10 siffror.")
        return False

age: int = calculate_age(birthday)
if check_age(age):
    

    def valid_telenum(telenum):
    # Kontrollerar om telefonnumret består av exakt 10 siffror
        if len(telenum) == 10 and telenum.isdigit():
            return True
        else:
            return False

    # Använder pyinputplus för att ta in användarens input
    
    while True:
        tele = py.inputStr('\nAnge ditt nummer: ')
        if check_number(tele):
            break
    # kollar att telefon nummret är giltigt. om inte så frågar den igen.



    färglista = ["Röd","Blå","Gul","Grön"]

    
    favorite_color: str = py.inputMenu(
        prompt="\nVilken är din favoritfärg?\n", choices=färglista, numbered=True
    )

    subscription = py.inputYesNo(prompt="\nVill du prenumerera hos oss? (YES/NO): ")


    print(f"""\n\nAnvändarnamn: {username}
E-postadress: {epost}
Födelsedatum: {birthday}
Ålder: {age}
Telenummer: {tele}
Prenumererar: {'Ja' if subscription == 'y' else 'Nej'}
Favoritfärg: {favorite_color} 
          """)
# Printar all information.



