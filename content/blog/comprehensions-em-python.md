Title: Comprehensions em Python: listas, dicionários e conjuntos de forma concisa
Date: 2026-08-25 09:00
Modified: 2026-08-25 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a usar list comprehensions, dict comprehensions e set comprehensions para escrever código Python mais limpo e conciso.

Você já escreveu um `for` para criar uma lista nova, iterando sobre outra lista e aplicando alguma transformação? Todo mundo já. O Python oferece uma forma mais enxuta de fazer isso: as **comprehensions**.

Comprehensions são uma sintaxe que permite criar listas, dicionários e conjuntos em uma única linha de código, de forma legível e expressiva. Quando usadas com moderação, deixam o código mais limpo e direto ao ponto.

## List comprehension

A forma básica funciona assim:

```python
# Forma tradicional
numeros = [1, 2, 3, 4, 5]
dobrados = []
for n in numeros:
    dobrados.append(n * 2)

# Comprehension
dobrados = [n * 2 for n in numeros]
# resultado: [2, 4, 6, 8, 10]
```

A sintaxe é `[expressao for item in iteravel]`. Pense como uma frase: "para cada item no iterável, aplique a expressão e guarde o resultado".

### Filtrando com条件

Você pode adicionar uma condição no final para filtrar elementos:

```python
# Números pares de uma lista
pares = [n for n in range(20) if n % 2 == 0]
# resultado: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Palavras com mais de 5 letras
palavras = ["python", "java", "javascript", "go", "ruby"]
longas = [p for p in palavras if len(p) > 5]
# resultado: ['python', 'javascript']
```

### Transformando e filtrando ao mesmo tempo

Você pode combinar transformação e filtro:

```python
# Dobrar apenas os números pares
resultado = [n * 2 for n in range(20) if n % 2 == 0]
# resultado: [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
```

### Comprehensions aninhadas

Em casos simples, você pode usar um `for` dentro de outro:

```python
# Achatando uma matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for linha in matriz for n in linha]
# resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Cuidado: comprehension aninhada pode ficar difícil de ler. Se ficar confuso,prefira o `for` tradicional.

## Dict comprehension

Funciona igual, mas cria um **dicionário**:

```python
# Criar um dicionário de平方
quadrados = {n: n**2 for n in range(1, 6)}
# resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Inverter um dicionário
origem = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in origem.items()}
# resultado: {1: 'a', 2: 'b', 3: 'c'}
```

### Filtrando dicionários

```python
# Notas acima de 7
notas = {"Ana": 9, "Bia": 6, "Carlos": 8, "Davi": 5}
aprovados = {nome: nota for nome, nota in notas.items() if nota >= 7}
# resultado: {'Ana': 9, 'Carlos': 8}
```

## Set comprehension

Cria um **conjunto** (sem duplicatas):

```python
# Pegar letras únicas de uma string
texto = "abracadabra"
letras = {c for c in texto}
# resultado: {'a', 'b', 'c', 'd', 'r'}
```

## Quando usar (e quando não usar)

**Use quando:**
- A lógica é simples e cabe em uma linha
- Você está criando uma lista/dict/set novo a partir de outro
- A comprehension é mais legível que o `for` equivalente

**Não use quando:**
- A lógica é complexa com múltiplas condições e transformações
- Você precisa de efeitos colaterais (como escrever em arquivo)
- A comprehension fica mais difícil de ler que o `for` tradicional

```python
# Exemplo OK: simples e claro
quadrados = [n**2 for n in range(10)]

# Exemplo ruim: complexo demais para uma linha
resultado = [
    transformar(a, b)
    for a in dados
    if a.valido
    for b in a.filhos
    if b.ativo and b.prioridade > 5
]
```

## Resumo

| Tipo | Sintaxe | Resultado |
|------|---------|-----------|
| List | `[x for x in iterable]` | Lista |
| Dict | `{k: v for k, v in iterable}` | Dicionário |
| Set | `{x for x in iterable}` | Conjunto |

Comprehensions são uma das ferramentas que fazem Python ser tão expressivo. Depois que você pega o jeito, usa o tempo todo — e seu código fica mais limpo por conta disso.
