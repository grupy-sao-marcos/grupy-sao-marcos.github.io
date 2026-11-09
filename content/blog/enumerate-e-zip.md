Title: enumerate e zip: laços mais elegantes em Python
Date: 2026-10-30 09:00
Modified: 2026-10-30 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Pare de usar range(len(...)) nos seus laços. Veja como enumerate e zip deixam o código mais limpo e mais pythônico.

Quem vem de outras linguagens costuma escrever laços assim em Python:

```python
frutas = ["maçã", "uva", "banana"]

for i in range(len(frutas)):
    print(i, frutas[i])
```

Funciona, mas o Python tem ferramentas feitas exatamente para isso.

## enumerate: índice e valor juntos

```python
for i, fruta in enumerate(frutas):
    print(i, fruta)
```

```
0 maçã
1 uva
2 banana
```

Quer começar a contar do 1? Use o parâmetro `start`:

```python
for posicao, fruta in enumerate(frutas, start=1):
    print(f"{posicao}º lugar: {fruta}")
```

## zip: percorrendo várias listas ao mesmo tempo

```python
nomes = ["Ana", "Bruno", "Carla"]
notas = [9.5, 7.0, 8.5]

for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")
```

O `zip` "costura" as listas, pegando um item de cada por vez.

## Criando dicionários com zip

```python
boletim = dict(zip(nomes, notas))
print(boletim)  # {'Ana': 9.5, 'Bruno': 7.0, 'Carla': 8.5}
```

## Cuidado com listas de tamanhos diferentes

Por padrão, o `zip` para na lista mais curta e ignora o resto **sem avisar**. A partir do Python 3.10 dá para pedir que ele reclame:

```python
nomes = ["Ana", "Bruno", "Carla"]
notas = [9.5, 7.0]

list(zip(nomes, notas))               # [('Ana', 9.5), ('Bruno', 7.0)]
list(zip(nomes, notas, strict=True))  # ValueError
```

## Combinando os dois

```python
for i, (nome, nota) in enumerate(zip(nomes, notas), start=1):
    print(f"{i}. {nome} tirou {nota}")
```

## Dica final

Sempre que escrever `range(len(...))`, pare e pense: provavelmente um `enumerate` ou um `zip` resolve de forma mais clara.

Contribua com novos artigos no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
