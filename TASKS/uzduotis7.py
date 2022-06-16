# Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu, tik datą (date.today()) 
# bei tik laiką (.now().time()).

from datetime import date, datetime, time


print(datetime.now())
print(type(date.today()))
print(datetime.today().time())

# š paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.

from datetime import datetime as data

print(data.today())




