Title: F-strings em Python: formatando textos do jeito fácil
Date: 2026-10-28 09:00
Modified: 2026-10-28 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a usar f-strings para montar textos, formatar números e datas e até depurar variáveis em Python.

Montar textos juntando variáveis é uma das tarefas mais comuns em qualquer programa. Em Python, a forma mais simples e legível de fazer isso são as **f-strings**.

## O básico

Basta colocar um `f` antes das aspas e as variáveis entre chaves:

```python
nome = "Ana"
idade = 30

print(f"{nome} tem {idade} anos")  # Ana tem 30 anos
```

Dentro das chaves vale qualquer expressão Python:

```python
preco = 19.9
quantidade = 3

print(f"Total: {preco * quantidade}")    # Total: 59.699999999999996
print(f"Nome em maiúsculas: {nome.upper()}")  # Nome em maiúsculas: ANA
```

## Formatando números

Aquele `59.699999999999996` não fica bonito. Depois do `:` você define o formato:

```python
total = 59.699999999999996

print(f"R$ {total:.2f}")       # R$ 59.70
print(f"{1234567.891:,.2f}")   # 1,234,567.89
print(f"{0.256:.1%}")          # 25.6%
print(f"{42:05d}")             # 00042
```

## Alinhando colunas

Ótimo para relatórios no terminal:

```python
produtos = [("Café", 18.5), ("Pão", 0.75), ("Queijo colonial", 42.0)]

for nome, preco in produtos:
    print(f"{nome:<18}{preco:>8.2f}")
```

```
Café                 18.50
Pão                   0.75
Queijo colonial      42.00
```

`<` alinha à esquerda, `>` à direita e `^` centraliza.

## Formatando datas

```python
from datetime import date

hoje = date(2026, 10, 28)
print(f"{hoje:%d/%m/%Y}")  # 28/10/2026
```

## O truque do `=` para depurar

A partir do Python 3.8, colocar `=` depois da variável mostra o nome e o valor:

```python
x = 10
y = 3

print(f"{x=}, {y=}, {x / y=:.2f}")  # x=10, y=3, x / y=3.33
```

Muito útil para aquele debug rápido.

## Dica final

Se você ainda usa `"Olá, " + nome + "!"` ou `"Olá, %s" % nome`, experimente as f-strings: o código fica mais curto, mais legível e mais rápido.

Sugira temas ou contribua no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
