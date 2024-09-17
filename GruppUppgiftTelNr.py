from gruppgift_telefonnummer_text import phone_number_text

number: int = 1  # Håller reda på antalet matchningar

for i in range(len(phone_number_text)):  # En for-loop som itererar över varje tecken i strängen
    phone_number: str = phone_number_text[i : i + 12]  # Tilldelar en sträng på 12 tecken från den aktuella positionen

    # En if-sats som kontrollerar att alla kriterier för ett giltigt telefonnummer uppfylls
    if (
        phone_number[0:3].isdecimal()
        and phone_number[5:7].isdecimal()
        and phone_number[9:13].isdecimal()
        and phone_number[3] == "-"
        and phone_number[7] == "-"
    ):
        print(f"{number}. {phone_number}")  # Printar telefonnumret och numret i ordningen
        number += 1  # Ökar räknaren för nästa giltiga telefonnummer
