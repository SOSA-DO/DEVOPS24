#guess the number
import random

random_number: int = random.randint(0,200)



while True:
    guess =int(input('Enter the number'))
    if guess == random_number:
        print('ACCESS GRANTED')
        break

    elif guess < random_number:
        print('To low. try again!')

    elif guess > random_number:
        print('To high. try again!')









#Moduler = Importera kod filer som "random" eller "math" "sys" "my_python_file"

#man kan importera funktioner från filerna genom att skriva "from" innan

#inte ha samma namn som standard moduler i koden, skapar förvirring. lista på moduler "print(help("modules"))"

#funktioner: Print() från kod till användare - Input() från användare till kod