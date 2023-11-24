import requests
from bs4 import BeautifulSoup

url = 'https://www.tabnews.com.br/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    for link in links:
        link_url = url + link.get('href')

        if link_url:
            link_response = requests.get(link_url)

            if link_response.status_code == 200:
                link_soup = BeautifulSoup(link_response.text, 'html.parser')

                try:
                    div_markdown = link_soup.find_all('div', class_='markdown-body')[-1]
                    content = div_markdown.get_text()

                    print(content)
                except:
                    print("Sem markdown em " + link_url)

            else:
                print(f'Falha na solicitação HTTP para {link_url}. Código de status: {link_response.status_code}')

else:
    print(f'Falha na solicitação HTTP para a página principal. Código de status: {response.status_code}')
