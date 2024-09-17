# • Skapa ett program som:
# • läser in en fil innehållandes topp 30 från OS i cykel 2024
# • hitta de tre snabbaste tiderna och skriv ut dom som ett podium
# • tiderna ska presenteras HH:MM:SS.sss
# • listan innehåller ett resultat för varje rad, ex: 
# • Glöm inte att använda dig att funktioner
# • En funktion ska utföra en uppgift!
# • modulen datetime (ingår i python standardlib) behöver användas
# • Läs själv på hur den fungerar och används
# • https://docs.python.org/3/library/datetime.html

# ta in med hjälp av open
# sortera efter tid
# .sort listor

# "C:\Users\gabbe\Downloads\TT_Olympic_2024_women.csv"

# import pathlib

# print(pathlib.Path.home())

women24 = r'C:\\Users\\gabbe\\Downloads\\TT_Olympic_2024_women.csv'
f = open(women24,'r',encoding='utf-8')

for rad in f:
    print(rad, end='')


# '''file = C:\Users\gabbe\Downloads\TT_Olympic_2024_women.csv

# with open('TT_Olympic_2024_women.csv', 'r') as file:
#     content: str = file.readlines()
#     print(content)'''