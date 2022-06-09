# from gettext import find
# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text

# # print(source)

# soup = BeautifulSoup(source, 'html.parser')     
# blokas = soup.find('div', class_ = 'headline')
# print(blokas.prettify())
# print("======") 

# blokas = soup.find("h3", class_ = "headline-title")
# blokas = blokas.find
# print(blokas.prettify())


# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find('div', class_ = 'headline')

# kategorija = blokas.find('div', class_ = 'headline-category').text.strip()

# tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
# print(kategorija)
# print(tekstas)

# Lietuvoje
# Kambarinės darbas už 300 eurų atrodė išsigelbėjimas: ką turės daryti, sužinojo tik atsidūrusi sutenerių poros bute

# from bs4 import BeautifulSoup   <----Kaip gauti visų blokų informaciją:
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_ = 'headline')

# for blokas in blokai:
#     try:
#         kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#         tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
#         print(kategorija)
#         print(tekstas)
#     except:
#         pass

# from bs4 import BeautifulSoup
# import requests
# import csv 

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_ = 'headline')

# with open("delfi naujienos.csv", "w", encoding="UTF-8", newline='') as failas:

#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['Kategorija', 'Tekstas'])
#     for blokas in blokai:
#         try:
#             kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#             tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
#             csv_writer.writerow([kategorija, tekstas])
#         except:
#             pass

#   Norimo gamintojo parduodamų telefonų išrinkimas iš svetainės

# import csv

# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai').text
# soup = BeautifulSoup(source, 'html.parser')

# blokai = soup.find_all('div', class_ = 'card card__product card--anim js-product-compare-product')

# with open("Telia telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

#     for blokas in blokai:
#         try:
#             pavadinimas = blokas.find('a', class_ = 'card__title js-product-name-truncate').text.strip()
#             men_kaina = blokas.find('div', class_ = 'pull-left').span.text.strip()
#             kaina = blokas.find('span', class_ = 'price--marker').next_element.next_element.next_element.next_element.span.text.strip()
#             csv_writer.writerow([pavadinimas, men_kaina, kaina])
#         except:
#             pass


# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/news/daily/world/karas-ukrainoje-rusu-ziniasklaida-ukrainoje-suciuptiems-britams-ir-marokieciui-mirties-bausme.d?id=90439595').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('p')
# # print(blokai[:8])
# blokai = blokai[1:8]
# # print(type(blokai))

# for blokas in blokai:
#     print(blokas.text.strip())

