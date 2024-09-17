# Strängmanipulation och RegEx --------------

# Kraftfulla redskap i scenarion där man behöver behandla stora mängder text
# Vanligt i scripts
# scripts är viktigt för devops
# scripts kan användas för att sätta igång andra program i datorn, 
# de är som små program. vi kommer gå igenom det mer

# Strängmanipulation --------------

#print('Please have a seat, I'll be there soon') -> x
print("Please have a seat, I'll be there soon") #-> ok

# Backslash eller Escape character "\" är ett special tecken sim inte behandlas som en instruktion av pyhton
# Exempel:
print('Please have a seat, I\'ll be there soon') #-> ok

# Det finns flera escape characters

print('Hej! vem är du?\nJag är jag')
#Hej! vem är du?
#Jag är jag

# man kan printa alla tecken i en sträng med"print(r')"

# multiline string print(''',''')

print('''Dear alice,
eves cat has been arrested.
sincerly,
policeman bob''')

#Dear alice,
#eves cat has been arrested.
#sincerly,
#policeman bob

#Strängindexering identifiering
#strängar är indexerade som listor eller tuplar.
#man kan dela upp strängar. det heter slicing.
my_string = 'Hello there'
print(my_string[0:5]) #kommer bara printa 'Hello'
print(my_string[0:7]) #kommer bara printa 'Hello t'

demo_str: str = 'testing'

#demo_str. #visar alla möjligheter med strängar

list_demo: list = [1,2]

#list_demo. #visar alla möjligheter med lists

#strängar är immutable
#a_str_var.upper använder man för att ändra alla bokstäver till stora bokstäver,
#det ändar inte strängen i sig det returnerar bara an kopia av strängen fast med stora bokstäver.
#Viktigt att spara returvärdet i en ny variabel om man ska använda det.

demo_str.isupper() #kollar om alla bokstäver är uppercase
demo_str.islower() #kollar om alla bokstäver är lowercase
demo_str.isalpha() #kollar om alla tecken är från alphabetet
demo_str.isdecimal() #kollar om alla tecken är nummer
#dessa returnerar booleans

demo_str.startswith #kollar om strängen startar med
demo_str.endswith #kollar om strängen slutar med

demo_str.join(list_demo) #tar emot en lista och sammanför det till en string
demo_str.split() #delar up allt till en lista

#padding och strip ---------------

#str.rjust(10, -) justerar åt höger i detta fall med 10 st '-' -> '----------hello'
#str.ljust() samma fast åt vänster

#str.lstrip() 
#str.rstrip()
#str.strip() tar bort onödig "padding" som blanksteg eller liknande


# --- PATTERN MATCHING --- 

#      - gruppövning - 

# --- RegEx --- Kap 7 i kursboken

import re #viktigt för att kunna använda reg ex

# regulära uttryck/Regular expressions
# mycket vanligt inom scripting
# man behöver inte komma ihåg regex patterns,
# det viktiga är att veta vad man kan göra med reg ex.
# man kan matcha en text med vilka regler man vill.
# viktigt att kunna detta som devops.

#search() #anropas med ett regex pattern och en sträng att skanna

re.compile() #kompilerar en pattern och sparar den i en variabel för återanvänding
# mycket mer effektivet för datorn

#gruppera matchningar med paranteser och group()
#alla matchningar får du i en tuple med group










