Title: Estruturas de dados em Python: listas, dicionários e conjuntos
Date: 2026-08-14 09:00
Modified: 2026-08-14 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Entenda na prática como funcionam as principais estruturas de dados nativas do Python e quando usar cada uma.

Quando começamos a programar em Python, uma das primeiras coisas que precisamos dominar são as **estruturas de dados**. Elas são as ferramentas que usamos para guardar e organizar informações dentro do nosso programa: uma lista de nomes, um cadastro de clientes, os itens de um carrinho de compras.

A boa notícia é que o Python já vem com estruturas prontas e muito poderosas. Vamos conhecer as quatro principais: **listas**, **tuplas**, **dicionários** e **conjuntos**.

## Listas

A lista é provavelmente a estrutura mais usada. Ela guarda elementos em uma ordem definida e permite duplicados, alterações e acesso por índice.

```python
frutas = ["banana", "maca", "uva"]
frutas.append("laranja")       # adiciona no final
frutas.insert(1, "manga")      # insere na posicao 1
frutas.remove("uva")           # remove pelo valor
frutas[0]                      # primeiro elemento -> "banana"
frutas[-1]                     # ultimo elemento -> "laranja"

print(len(frutas))             # 3
```

Para percorrer uma lista, usamos um laço `for`:

```python
for fruta in frutas:
    print(fruta)
```

E para criar listas de forma rápida, existe o famoso **list comprehension**:

```python
dobros = [numero * 2 for numero in range(10)]
print(dobros)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## Tuplas

A tupla é parecida com a lista, mas é **imutável**: depois de criada, não dá para adicionar, remover ou alterar elementos. Essa característica é útil quando queremos garantir que um dado não mude, como coordenadas ou configurações fixas.

```python
coordenadas = (-21.9, -49.6)  # latitude e longitude

# coordenadas.append(0)  # erro! tuplas nao aceitam alteracao
```

Uma "pegadinha" clássica é usar uma vírgula para criar uma tupla de um elemento:

```python
sozinho = ("sp",)   # tupla com 1 elemento
errado = ("sp")     # string, nao uma tupla!
```

Tuplas também são usadas para "desempacotar" valores, o que torna o código bem elegante:

```python
latitude, longitude = coordenadas
print(latitude)   # -21.9
```

## Dicionários

O dicionário guarda pares de **chave** e **valor**. É a estrutura ideal para representar coisas do mundo real, como um cadastro:

```python
usuario = {
    "nome": "Maria",
    "idade": 28,
    "linguagens": ["Python", "JavaScript"],
}

print(usuario["nome"])        # Maria
usuario["cidade"] = "São Marcos"   # adiciona um novo campo

for chave, valor in usuario.items():
    print(chave, "->", valor)
```

Para acessar um valor que talvez não exista, prefira o método `get`, que evita erros:

```python
print(usuario.get("telefone"))        # None (nao existe)
print(usuario.get("telefone", "nao informado"))  # valor padrao
```

## Conjuntos (sets)

O conjunto guarda elementos **únicos** e sem ordem definida. Ele é perfeito para eliminar duplicatas e fazer operações de comparação.

```python
participantes_dia1 = {"Ana", "Pedro", "Lucas"}
participantes_dia2 = {"Lucas", "Julia", "Ana"}

unicos = participantes_dia1 | participantes_dia2      # uniao
ambos = participantes_dia1 & participantes_dia2       # intersecao

print(ambos)  # {'Lucas', 'Ana'}
```

Eliminar duplicatas de uma lista nunca foi tão simples:

```python
lista_com_repeticoes = [1, 2, 2, 3, 3, 3]
sem_duplicatas = list(set(lista_com_repeticoes))
print(sem_duplicatas)  # [1, 2, 3]
```

## Quando usar cada uma?

| Estrutura   | Ordenada | Mutável | Aceita duplicados | Bom para                          |
|-------------|----------|---------|-------------------|-----------------------------------|
| Lista       | Sim      | Sim     | Sim               | sequências que mudam              |
| Tupla       | Sim      | Não     | Sim               | dados fixos e agrupados           |
| Dicionário  | Sim*     | Sim     | chaves não        | buscar por nome/chave             |
| Conjunto    | Não      | Sim     | Não               | elementos únicos e comparações    |

*\*Desde o Python 3.7 os dicionários mantêm a ordem de inserção.*

Dominar essas estruturas resolve a maioria dos problemas do dia a dia. O truque é pensar no dado que você precisa guardar e escolher a ferramenta certa. Nos próximos artigos vamos usar bastante essas estruturas em exemplos reais.

Tem alguma dúvida ou sugestão de tema? Deixe nos comentários ou contribua com um artigo no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
