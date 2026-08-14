Title: Automatizando tarefas do dia a dia com Python
Date: 2026-08-15 09:00
Modified: 2026-08-15 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a usar o Python para automatizar tarefas repetitivas do seu dia a dia, como renomear arquivos, organizar pastas e gerar relatórios.

Quantas vezes você já perdeu tempo fazendo tarefas repetitivas no computador: renomear dezenas de arquivos, organizar fotos em pastas, converter um monte de arquivos, montar um relatório manualmente?

O Python é uma excelente ferramenta para **automação**. Com algumas linhas de código, você transforma tarefas que levariam horas em algo que roda em segundos. Vamos ver exemplos práticos que você pode adaptar para o seu caso.

## Trabalhando com arquivos e pastas

O módulo `os` e `shutil` são os pilares para manipular arquivos no Python.

### Renomear vários arquivos de uma vez

Imagine que você tem várias fotos chamadas `IMG_2026_001.jpg`, `IMG_2026_002.jpg` e quer renomeá-las para algo mais organizado:

```python
import os

caminho = "minhas_fotos"
for arquivo in os.listdir(caminho):
    if arquivo.endswith(".jpg"):
        novo_nome = arquivo.replace("IMG_2026_", "ferias_")
        os.rename(
            os.path.join(caminho, arquivo),
            os.path.join(caminho, novo_nome),
        )
print("Arquivos renomeados com sucesso!")
```

### Organizar arquivos em pastas

Que tal separar os downloads por tipo de arquivo? Uma automação clássica:

```python
import os
import shutil

def organizar(pasta):
    categorias = {
        ".jpg": "imagens", ".png": "imagens", ".gif": "imagens",
        ".pdf": "documentos", ".docx": "documentos",
        ".mp3": "musica", ".mp4": "videos",
    }
    for arquivo in os.listdir(pasta):
        origem = os.path.join(pasta, arquivo)
        if not os.path.isfile(origem):
            continue
        extensao = os.path.splitext(arquivo)[1].lower()
        destino = categorias.get(extensao, "outros")
        destino_path = os.path.join(pasta, destino)
        os.makedirs(destino_path, exist_ok=True)
        shutil.move(origem, os.path.join(destino_path, arquivo))

organizar("downloads")
```

## Lendo e escrevendo arquivos de texto

A automação de relatórios geralmente envolve ler dados de um arquivo e gerar outro. Vamos somar os valores de uma planilha simples em texto:

```python
total = 0
with open("vendas.txt", encoding="utf-8") as arquivo:
    for linha in arquivo:
        valor = linha.strip()
        if valor.isdigit():
            total += int(valor)

with open("resumo.txt", "w", encoding="utf-8") as saida:
    saida.write(f"Total de vendas: {total}\n")

print(f"Relatorio gerado, total: {total}")
```

Perceba o uso do `with`: ele garante que o arquivo seja fechado corretamente, mesmo se ocorrer um erro no meio.

## Trabalhando com datas e agendamento

O módulo `datetime` permite trabalhar com datas facilmente:

```python
from datetime import datetime, timedelta

hoje = datetime.now()
amanha = hoje + timedelta(days=1)

print(hoje.strftime("%d/%m/%Y %H:%M"))  # 14/08/2026 09:00
print("Amanha:", amanha.strftime("%d/%m/%Y"))
```

## Buscando dados na web

Para tarefas que dependem de informações online, usamos a biblioteca `requests`. Por exemplo, consultar a cotação de uma moeda:

```python
import requests

resposta = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
dados = resposta.json()
cotacao_brl = dados["rates"]["BRL"]

print(f"1 USD vale R$ {cotacao_brl:.2f}")
```

Lembre-se de instalar a biblioteca com `pip install requests` (veja como gerenciar dependências no nosso [artigo sobre ambientes virtuais]({filename}virtual-env.md)).

## Dica: use o `pathlib`

Desde o Python 3.4 existe o `pathlib`, que deixa o trabalho com caminhos muito mais legível e moderno:

```python
from pathlib import Path

pasta = Path("minhas_fotos")
for arquivo in pasta.glob("*.jpg"):
    print(arquivo.stem)  # nome sem extensao
```

## Começando do simples

A melhor forma de aprender automação é começando pequeno. Escolha uma tarefa que você faz toda semana e tente automatizar:

1. Liste os passos que você faz manualmente;
2. Quebre o problema em pequenas partes;
3. Teste cada parte isolada no terminal;
4. Junte tudo e rode o script completo.

Com o tempo, você vai perceber que o Python não serve apenas para construir grandes sistemas, mas também para **eliminar o trabalho repetitivo** e dar mais tempo para o que realmente importa.

Tem alguma automação que você gostaria de ver por aqui? Sugira nos comentários ou contribua com um artigo no nosso [repositorio](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
