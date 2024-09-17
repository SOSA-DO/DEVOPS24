#- LEKTION 3 NOTES -

# data strukturer är strukture om hur man samlar data. ex: 'List' 

#list:
#animal1: str = 'cat'
#animal2: str = 'mouse'


animals: list = ['cat', 'mouse', 'dog']
#                  0       1       2
print('i am ' + animals[2])

#animals.remove('värde') = ta bort värde - bra att använda i större program för att inte riskera stt ta bort fel index.

#del(animals[värde]) = lättare för datorn att köra än ovan

#animals[2] = 'nytt värde' = byter ut värde.

#animals.append('värde') = lägger till nytt värde '

#animals.instert

#list + for loop == sant

#for animal in animals = printar hela listan i ordning

#'in operator' = print(cat in animals) = boolean (True)
#print(house in animals) = False

#'not in operator' = samma som uppe vast tvärtom

#list.sort() = sorterar listan i bokstavsordning, stor bokstav gå alltid först. 
#funkar även med integers men ej med både str och int

#mutable kan förändras - 
#immutable kan inte förändras - kan ändras men förändras inte 

#hexadecimaler används som "adress" för minnesplatsen för t.ex. variabler.
#>>> hex(id(list))

#tuple - som en lista en säker. oförändringsbar. bra för viktiga saker som bör vara samma. 
#det går inte att lägga till byta ut eller ta bort från tuple.

#dictionary
# variabel: dict = {'key': 'value', 'size': 'big'}
#variable.get('key') -> ger 'value'

#nyckeln (key) måste vara immutable

#values() ger en samling av alla värden
#keys() ger alla keys
#items() ger en tuple med både keys och values

#funkar bra i 'for loopar'