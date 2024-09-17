# worldwide web

# virtuell stad där man komunicerar i 1or och 0or och webbläsaren översätter till text och bilder.
# http grundläggande nätverksprotokollet som är störst idag
# http status codes: 200 = ok/succes 404 = page not found

# url = länk
# url är adressen till webbplatsen. det är en GET-request

# klient -> server
# klienten är den som vill hämata något till exempel en webbsida från en server
# klienten komunicerar till servern via internet

# API Application Programming Interface
# hemsidor och organisationer bygger api:er för att klienter ska kunna använda de. - till exepel smhi kan ge väder data.

# Json Data
# en plattforms oberoende syntax för att representera data
# har sex data typer - 1 string 2 number 3 boolean 4 array 5 json object 6 null
# standariserat sätt att överföra data.
# även vanligt format för config-filer som pyhton

# import json
# import requests 
#-------------------------------------------------------------------------------


# Variables
$USERNAME = "ditt användarnamn"
$REPO_NAME = "ditt reponamn"
$TOKEN = "klistra in token från github här"  # Replace with your actual token
$GITHUB_URL = "https://$USERNAME:$TOKEN@github.com/$USERNAME/$REPO_NAME.git"

# Step 1: Clone the empty GitHub repository
git clone $GITHUB_URL
Set-Location -Path $REPO_NAME

# Step 2: Create a simple Python file
"print('Hello, GitHub!')" | Out-File -Encoding UTF8 -FilePath hello.py

# Step 3: Skriv en enkel README
"# Programmering1-2024`nThis repository contains examples for the Programmering1-2024 course." | Out-File -Encoding UTF8 -FilePath README.md

# Step 4: Lägg till de filer vi skapat för staging - redo att commita och skickas upp
git add hello.py README.md

# Step 5: Commit med ett meddelande
git commit -m "Initial commit: Add hello.py and README.md"

# Step 6: Pusha till main-branchen
git push origin main

# Placera scriptet i ditt working directory, ämnat för att bli ett lokalt repo
# Se till att scriptet är exekverbart(skriv detta i powershell): Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# Kör scriptet ståendes i ditt working directory: .\init_with_windows.ps1