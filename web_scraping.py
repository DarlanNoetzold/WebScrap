import requests
from bs4 import BeautifulSoup

# URL do site a ser extraído
url = 'https://www.tabnews.com.br/'

# Enviar uma solicitação HTTP para o site
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Encontre todas as tags <a> dentro de <article> com um atributo href que começa com '/'
for a_tag in soup.select('article a[href^="/"]'):
    title = a_tag.text
    print(title)