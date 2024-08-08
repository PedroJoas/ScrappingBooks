import re
import requests
from bs4 import BeautifulSoup
from Livro import Livro


# organizar as urls de cada página
url = 'https://books.toscrape.com/catalogue/page-{}.html'

urls = [url.format(pagina) for pagina in range(1,51)]

# Requisição usando uma sessão
with requests.Session() as session:
    for url in urls:
        try:
            response = session.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
        
            # Pegar article dos livros
            articles = soup.findAll('article', attrs={'class': 'product_pod'})
            for article in articles:    
                # Pegar titulo
                title = article.find('h3').find('a')['title']
                
                # Pegar review
                review = article.find('p')['class'][1]


                # Pegar preço
                preco = article.find('p', attrs={'class':'price_color'}).text

                preco = re.findall('[\d.]+', preco)[0]


                # Pegar URL
                url_img = article.find('div').find('a')['href']

                # Classe
                livro = Livro(title, review, preco, url_img)

                # Linha do arquivo

                linha = f'{livro.get_titulo()},{livro.get_review()},{livro.get_preco()},{livro.get_url_img()}'

                with open('livros.csv', 'a', newline='') as file:
                    file.write(linha + '\n')


        except requests.HTTPError as e:
            print(f'Erro HTTP: {e}')
