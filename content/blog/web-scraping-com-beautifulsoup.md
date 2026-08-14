Title: Web scraping com Python e BeautifulSoup: extraindo dados da web
Date: 2026-08-21 09:00
Modified: 2026-08-21 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a extrair informações de páginas web automaticamente usando requests e BeautifulSoup, com boas práticas e cuidado com a ética.

Imagina que você precisa coletar os preços de produtos de um site para comparar, ou montar uma lista com os títulos de notícias de um portal. Fazer isso manualmente é inviável, mas o Python pode fazer por você em segundos.

**Web scraping** é a técnica de extrair dados de páginas web de forma automatizada. Neste artigo vamos usar duas bibliotecas muito populares: o `requests` para baixar a página e o `BeautifulSoup` para analisar o HTML.

## Instalando as dependências

```bash
pip install requests beautifulsoup4
```

## Entendendo o HTML

Todo site é feito de HTML, e cada elemento é marcado com *tags*. Por exemplo:

```html
<ul>
    <li class="produto">Notebook por R$ 2.999,00</li>
    <li class="produto">Monitor por R$ 899,00</li>
</ul>
```

O BeautifulSoup transforma esse texto em uma estrutura navegável, e nós "procuramos" pelos elementos que nos interessam usando seletores parecidos com os do CSS.

## Primeiro scraping

Vamos extrair os títulos dos artigos do blog do próprio site da comunidade:

```python
import requests
from bs4 import BeautifulSoup

resposta = requests.get("https://grupy-sao-marcos.github.io/blog/")
pagina = BeautifulSoup(resposta.text, "html.parser")

for artigo in pagina.select("h1, h2"):
    print(artigo.get_text(strip=True))
```

O que aconteceu aqui:

- `requests.get(...)` baixa o conteúdo da página;
- `BeautifulSoup(resposta.text, "html.parser")` transforma o HTML em um objeto navegável;
- `.select("h1, h2")` encontra todos os elementos de título;
- `.get_text(strip=True)` extrai somente o texto, removendo espaços extras.

## Encontrando elementos específicos

A tag sozinha muitas vezes não basta, pois as páginas têm dezenas de elementos. Por isso usamos **classes**, **ids** e atributos para refinar a busca:

```python
# busca por classe CSS
produtos = pagina.select(".produto")

# busca por id
menu = pagina.select_one("#menu")

# busca por atributo
links = pagina.select('a[href*="python"]')
```

O `select_one` retorna apenas o primeiro elemento, enquanto o `select` retorna uma lista.

## Exemplo completo: extraindo notícias

Vamos imaginar uma página com notícias. A estrutura HTML poderia ser:

```html
<article class="noticia">
    <h2 class="titulo">Python 3.13 é lançado</h2>
    <p class="data">Publicado em 10/08/2026</p>
    <a href="/noticias/python-3-13">Leia mais</a>
</article>
```

Nosso script:

```python
import requests
from bs4 import BeautifulSoup

resposta = requests.get("https://exemplo.com/noticias")
pagina = BeautifulSoup(resposta.text, "html.parser")

noticias = []
for item in pagina.select("article.noticia"):
    titulo = item.select_one(".titulo").get_text(strip=True)
    data = item.select_one(".data").get_text(strip=True)
    link = item.select_one("a")["href"]

    noticias.append({"titulo": titulo, "data": data, "link": link})

for noticia in noticias:
    print(noticia)
```

Repare em `item.select_one("a")["href"]`: além do texto, também conseguimos acessar os **atributos** de um elemento usando `["nome_do_atributo"]`.

## Lidando com páginas dinâmicas

Muitos sites modernos carregam o conteúdo via JavaScript depois que a página abre. Nesse caso, o `requests` só enxerga o HTML "vazio" e o scraping não encontra os dados.

Para esses casos existem ferramentas mais poderosas, como o **Selenium** ou o **Playwright**, que controlam um navegador de verdade:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch()
    pagina = navegador.new_page()
    pagina.goto("https://exemplo.com/noticias")
    conteudo = pagina.content()
    navegador.close()
```

## Boas práticas e ética

Web scraping exige responsabilidade. Siga sempre estas regras:

1. **Consulte o `robots.txt`** do site (`https://exemplo.com/robots.txt`) para saber se o scraping é permitido naquele caminho;
2. **Seja gentil**: adicione um pequeno intervalo entre uma requisição e outra com `time.sleep()`;
3. **Respeite os termos de uso** do site e a legislação (a LGPD protege dados pessoais);
4. **Use APIs oficiais** sempre que existirem — são o caminho correto e estável;
5. **Identifique-se** com um `User-Agent` que mostre quem você é e seu propósito.

Exemplo de um script gentil e identificado:

```python
import time

import requests
from bs4 import BeautifulSoup

cabecalhos = {
    "User-Agent": "Bot de estudo - contato@exemplo.com"
}

urls = [
    "https://exemplo.com/pagina1",
    "https://exemplo.com/pagina2",
]

for url in urls:
    resposta = requests.get(url, headers=cabecalhos)
    if resposta.status_code == 200:
        pagina = BeautifulSoup(resposta.text, "html.parser")
        print(pagina.title.get_text())
    time.sleep(2)
```

O `status_code == 200` verifica que a página foi retornada com sucesso antes de tentar analisá-la.

## Onde usar na vida real

- Montar listas de **preços** para comparação (sempre dentro das regras);
- Coletar **notícias** e gerar resumos;
- Automatizar a **coleta de dados públicos** de órgãos governamentais;
- Criar **backups de conteúdo**;
- Alimentar **análises de dados**.

## Lembre-se

Scraping é uma ferramenta incrível, mas use-a com **responsabilidade**: para aprender, para dados públicos e sempre respeitando o dono do site. Quando houver uma API oficial, ela é sempre a melhor opção.

Quer ver mais exemplos de automação? Sugira nos comentários ou contribua com um artigo no nosso [repositorio](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
