# Sukurti programą, kuri:

# Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba 
# (data būtų nustatoma automatiškai, pagal dabartinę datą).
# Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
# Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.


def do_smt() -> None:
        name = input('Please enter your name: ')
        birthday = input('Please enter your bithday: ')
        occupation = input('Please enter your occupation: ')
        salary = input('Please enter your salary: ')
        start_date = input('Please enter your start date: ')

        print(f"My personal info is: {name} - {birthday} - {occupation} - {salary} - {start_date}")

