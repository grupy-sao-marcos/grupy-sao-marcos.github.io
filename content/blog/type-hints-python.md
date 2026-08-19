Title: Type hints em Python: escrevendo código mais claro e seguro
Date: 2026-08-17 09:00
Modified: 2026-08-17 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a usar type hints (anotações de tipo) para deixar seu código Python mais legível, auto documentado e com menos bugs.

Python é uma linguagem de tipagem dinâmica: você não precisa declarar o tipo de uma variável, e o mesmo valor pode mudar de tipo no meio do caminho. Isso deixa o código rápido de escrever, mas pode virar fonte de bugs quando o projeto cresce.

Os **type hints** (anotações de tipo) surgiram justamente para resolver isso. Eles não mudam a forma como o Python roda, mas deixam o código muito mais claro e permitem que ferramentas encontrem erros **antes** de você executar o programa.

## Anotando funções

O uso mais comum é anotar os parâmetros e o retorno de uma função:

```python
def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)


def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"
```

Perceba que agora qualquer pessoa que ler a função sabe que `peso` e `altura` devem ser números e que o resultado também será um número.

## Tipos de coleções

Para listas, dicionários e afins, usamos o módulo `typing` (no Python 3.9+ você também pode usar `list[...]` e `dict[...]` diretamente):

```python
from typing import Optional, Union


def somar_lista(numeros: list[float]) -> float:
    return sum(numeros)


def buscar_usuario(codigo: int) -> Optional[dict]:
    # retorna None quando o usuario nao existe
    ...


def formatar_valor(valor: Union[int, float]) -> str:
    return f"R$ {valor:.2f}"
```

Vamos entender cada um:

- `list[float]` indica uma lista onde todos os elementos são `float`;
- `Optional[dict]` significa que a função pode retornar um `dict` **ou** `None`;
- `Union[int, float]` aceita inteiro **ou** float.

## Novidades do Python 3.10

A partir do Python 3.10 existem atalhos mais legíveis: `|` no lugar de `Union` e `Optional`.

```python
def formatar_valor(valor: int | float) -> str:
    return f"R$ {valor:.2f}"


def buscar_usuario(codigo: int) -> dict | None:
    ...
```

## Type hints em variáveis

Também é possível anotar variáveis, o que ajuda em códigos maiores:

```python
nome: str = "Maria"
precos: list[float] = [19.90, 7.50]
```

## Dataclasses: dados estruturados com tipos

Para representar um "modelo" de dados, as **dataclasses** combinam muito bem com type hints:

```python
from dataclasses import dataclass


@dataclass
class Usuario:
    nome: str
    idade: int
    email: str | None = None


maria = Usuario(nome="Maria", idade=28)
print(maria.nome)   # Maria
print(maria.idade)  # 28
```

Além de deixar os dados organizados, a dataclass gera automaticamente o `__init__` e uma representação legível da classe.

## Os type hints são opcionais?

Sim, o interpretador Python **ignora** as anotações na hora de rodar o código. Elas não criam verificação em tempo de execução:

```python
def dobrar(valor: int) -> int:
    return valor * 2


print(dobrar("abc"))  # vai rodar, mas "abc" * 2 = "abcabc" (errado!)
```

Para que os type hints realmente façam a verificação, usamos ferramentas de análise estática como o **mypy**:

```bash
pip install mypy
mypy meu_arquivo.py
```

O mypy lê seu código e aponta exatamente onde os tipos não batem:

```bash
meu_arquivo.py:1: error: Argument 1 to "dobrar" has incompatible type "str"; expected "int"
```

É como ter um "linter de tipos": ele encontra uma classe inteira de bugs sem precisar rodar o programa.

## Vale a pena usar?

Depende do tamanho do projeto. Em scripts pequenos, anotações podem ser exagero. Mas em projetos que crescem, que são mantidos por várias pessoas ou que viram bibliotecas, os benefícios são enormes:

- O código fica **auto documentado**;
- Editores como VS Code e PyCharm usam os tipos para dar **autocompletar** e alertas;
- O **mypy** (e ferramentas similares) pega bugs antes de rodar;
- O time inteiro ganha clareza sobre o que cada função espera e retorna.

## Dica final

Comece anotando as **funções públicas** e as **dataclasses** dos seus projetos. Não precisa anotar tudo de uma vez — aos poucos a prática vira hábito e a qualidade do código melhora naturalmente.

Gostou do tema? Em breve escreveremos sobre testes automatizados, outro pilar das boas práticas. Sugira temas ou contribua no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
