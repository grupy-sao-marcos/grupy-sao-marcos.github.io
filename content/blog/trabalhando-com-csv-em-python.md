Title: Trabalhando com CSV em Python: dados de tabelas sem complicação
Date: 2026-08-22 09:00
Modified: 2026-08-22 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a ler, filtrar e gerar arquivos CSV com o módulo csv da biblioteca padrão do Python, sem instalar nada.

Planilhas e bancos de dados costumam ser exportados para um formato chamado **CSV** (*Comma-Separated Values*). É um arquivo de texto simples onde cada linha é um registro e cada coluna é separada por vírgula:

```text
nome,idade,cidade
Maria,28,Sao Marcos
Joao,35,Espirito Santo do Pinhal
Ana,22,Casa Branca
```

Apesar de simples, o CSV está em todo lugar: relatórios financeiros, listas de clientes, dados de sensores, exportações de sistemas. E o Python tem um módulo nativo chamado `csv` que facilita (e muito) o trabalho com esses arquivos.

## Lendo um arquivo CSV

Para ler, usamos a função `csv.reader`. Cada linha vira uma **lista** de valores:

```python
import csv

with open("dados.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
```

Resultado:

```text
['nome', 'idade', 'cidade']
['Maria', '28', 'Sao Marcos']
['Joao', '35', 'Espirito Santo do Pinhal']
```

O `newline=""` é importante para evitar linhas em branco indesejadas entre os registros, um problema clássico de quem usa CSV no Python.

## Usando dicionários: csv.DictReader

Trabalhar com listas é confuso quando a planilha tem muitas colunas. O `csv.DictReader` resolve isso transformando cada linha em um **dicionário**, usando a primeira linha como nome das colunas:

```python
import csv

with open("dados.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha["nome"], "-", linha["cidade"])
```

Agora acessamos cada valor pelo nome da coluna, o que torna o código muito mais legível e seguro.

## Filtrando dados

Com dicionários, filtrar fica natural. Vamos listar apenas os registros de pessoas com mais de 25 anos:

```python
import csv

with open("dados.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        if int(linha["idade"]) > 25:
            print(linha["nome"])
```

Repare no `int(linha["idade"])`: tudo que vem de um CSV é **texto**, então precisamos converter para número antes de comparar.

## Escrevendo um CSV

Para gerar um arquivo, usamos `csv.writer`:

```python
import csv

cabecalho = ["nome", "idade", "cidade"]
registros = [
    ["Maria", 28, "Sao Marcos"],
    ["Joao", 35, "Espirito Santo do Pinhal"],
]

with open("saida.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(cabecalho)      # uma linha
    escritor.writerows(registros)     # varias linhas de uma vez
```

O `csv.writer` cuida de tudo para você: coloca as vírgulas, escapa valores que contenham vírgula ou aspas e usa quebra de linha corretamente.

## Escrevendo com dicionários: csv.DictWriter

De forma análoga, o `csv.DictWriter` grava listas de dicionários. A vantagem é que ele só escreve as colunas que você definir em `fieldnames`:

```python
import csv

cabecalho = ["nome", "idade", "cidade"]
registros = [
    {"nome": "Maria", "idade": 28, "cidade": "Sao Marcos"},
    {"nome": "Joao", "idade": 35, "cidade": "Espirito Santo do Pinhal"},
]

with open("saida.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
    escritor.writeheader()
    escritor.writerows(registros)
```

O `writeheader()` grava a primeira linha com os nomes das colunas automaticamente.

## Delimitadores diferentes

Nem todo CSV usa vírgula. No Brasil é comum encontrar arquivos separados por ponto e vírgula (`;`), porque a vírgula é usada como separador decimal. Basta informar o delimitador:

```python
with open("dados_br.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    for linha in leitor:
        print(linha)
```

Se o arquivo estiver com texto corrompido, lembre-se do `encoding="utf-8"` e, se necessário, `encoding="latin-1"`.

## Exemplo completo: relatório de vendas

Vamos juntar tudo: ler uma planilha de vendas, calcular o total por vendedor e salvar um resumo:

```python
import csv

total_por_vendedor = {}

with open("vendas.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        vendedor = linha["vendedor"]
        valor = float(linha["valor"])
        total_por_vendedor[vendedor] = total_por_vendedor.get(vendedor, 0.0) + valor

with open("resumo_vendas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["vendedor", "total"])
    for vendedor, total in total_por_vendedor.items():
        escritor.writerow([vendedor, f"{total:.2f}"])

print("Resumo gerado!")
```

Em poucas linhas: lemos os dados, agrupamos por vendedor e geramos um novo arquivo pronto para ser aberto em qualquer planilha.

## E se eu precisar de arquivos .xlsx?

O módulo `csv` trabalha com texto puro. Para planilhas Excel nativas (`.xlsx`), o formato é outro e usamos bibliotecas como `openpyxl` ou `pandas`. É um bom assunto para um próximo artigo de dados.

## Resumo

O módulo `csv` resolve a grande maioria dos casos de leitura e escrita de tabelas:

- `csv.reader` e `csv.writer` para trabalhar com listas;
- `csv.DictReader` e `csv.DictWriter` para trabalhar com dicionários;
- Sempre use `newline=""` e `encoding="utf-8"`;
- Atenção ao delimitador (`delimiter=";"`).

Com isso você pode automatizar a troca de dados entre sistemas, gerar relatórios e alimentar análises — tudo com a biblioteca padrão do Python.

Usou o CSV em alguma automação interessante? Conta pra gente nos comentários ou contribua com um artigo no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
